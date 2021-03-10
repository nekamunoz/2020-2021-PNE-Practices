from pathlib import Path
import termcolor

def seq_ping():
    print("OK")


def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")


def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict


def seq_reverse(seq):
    reverse_seq = seq[::-1]
    return reverse_seq


def seq_complement(seq):
    complement = ""
    for d in seq:
        if d == "A":
            complement += "T"
        elif d == "T":
            complement += "A"
        elif d == "G":
            complement += "C"
        else:
            complement += "G"
    return complement


def seq_frequent(dict_count):
    return max(dict_count, key=dict_count.get)


class Seq:
    def __init__(self, str_bases):
        if Seq.is_valid_seq2(str_bases):
            self.str_bases = str_bases
            print("New sequence created!")
        else:
            self.str_bases = "ERROR"
            print("INCORRECT Sequence detected.")

    @staticmethod
    def is_valid_seq2(str_bases):
        for i in str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            text = "Sequence" + str(i) + "(Length: " + str(seq_list[i].len()) + "):" + str(seq_list[i])
            termcolor.cprint(text, "red")

    def is_valid_seq(self):
        for i in self.str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def __str__(self):
        return self.str_bases

    def len(self):
        return len(self.str_bases)


def generate_seqs(pattern, number):
    seq = []
    for e in range(0, number):
        seq.append(Seq(pattern * (e + 1)))
    return seq
