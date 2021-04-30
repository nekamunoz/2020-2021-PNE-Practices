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






def info(cs, seq):
    print_colored("INFO", "yellow")
    s1 = Seq(seq)
    count_bases = s1.count_bases()
    nucleotides = ("A", "C", "G", "T")
    percentage = s1.percentage_base(count_bases, s1.len())
    response1 = "Sequence: " + str(s1) + "\nTotal length: " + str(s1.len()) + "\n"
    print(response1)
    i = 0
    response2 = ""
    for i in range(0, len(count_bases)):
        response2 += nucleotides[i] + ": " + str(count_bases[i]) + " (" + percentage[i] + ")\n"
        i += 1
    print(response2)
    cs.send((response1 + response2).encode())


def comp(cs, seq):
    print_colored("COMP", "green")
    s1 = Seq(seq)
    response = "Complement: " + s1.complement() + "\n"
    print(response.replace("\n",""))
    cs.send(response.encode())


def rev(cs, seq):
    print_colored("REV", "green")
    s1 = Seq(seq)
    response = "Reverse: " + s1.reverse() + "\n"
    print(response.replace("\n",""))
    cs.send(response.encode())




