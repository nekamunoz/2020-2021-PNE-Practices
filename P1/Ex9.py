from Seq1 import Seq


def print_result(i, sequence):
    print("Sequence " + " (Length: " + str(sequence.len()) + "): " + str(sequence))
    print("Bases: ", sequence.count())
    print("Rev: ", sequence.reverse())
    print("Comp: ", sequence.complement())


PROJECT_PATH = "../P0/sequences/"
print("-----| Exercise 9 |-----")
s1 = Seq()
s1.read_fasta(PROJECT_PATH + "ADA.txt")
print_result("",s1)

