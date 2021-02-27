from pathlib import Path


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

