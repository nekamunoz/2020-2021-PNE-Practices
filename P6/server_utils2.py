from Seq1 import Seq
from urllib.parse import urlparse, parse_qs
import jinja2
import pathlib


def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message,color))


def read_template_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())


def get(list_sequences, seq_number):
    context = {
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]}
    contents = read_template_html_file("html/get.html").render(context=context)
    return contents


def gene(seq_name):
    PATH = "./sequences/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.str_bases
    }
    content = read_template_html_file("html/gene.html").render(context=context)
    return content


def operation(seq, op):
    if op == "Info":
        context = info(seq)
    elif op == "Comp":
        context = comp(seq)
    elif op == "Rev":
        context = rev(seq)
    context["sequence"] = seq
    context["op_name"] = op
    content = read_template_html_file("html/operation.html").render(context=context)
    return content


def info(seq):
    s1 = Seq(seq)
    count_bases = s1.count_bases()
    nucleotides = ("A", "C", "G", "T")
    percentage = s1.percentage_base(count_bases, s1.len())
    i = 0
    percentage_bases = ""
    for i in range(0, len(count_bases)):
        percentage_bases += nucleotides[i] + ": " + str(count_bases[i]) + " (" + percentage[i] + ")"
        i += 1
    context = {
        "result": [s1.len, percentage_bases]
    }
    return context



def comp(seq):
    s1 = Seq(seq)
    context = {
        "result": s1.complement()
    }
    return context


def rev(seq):
    s1 = Seq(seq)
    context = {
        "result": s1.reverse()
    }
    return context


