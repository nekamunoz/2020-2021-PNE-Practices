from Seq1 import Seq


def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message,color))


def format_command(command):
    return command.replace("\n","").replace("\r","")


def ping(cs):
    print_colored("PRINT", "green")
    response = "OK!\n"
    print(response)
    cs.send(str(response).encode())


def get(cs, list_sequences, seq_number):
    print_colored("GET", "yellow")
    try:
        response = list_sequences[int(seq_number)] + "\n"
        print(response)
    except IndexError:
        response = "ERROR: no sequence with index " + str(seq_number) + ".\n"
        print(response)
    cs.send(response.encode())


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


def gene(cs, seq_name):
    print_colored("GENE", "green")
    PATH = "../P0/sequences/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    print(s1)
    cs.send((str(s1) + "\n").encode())

