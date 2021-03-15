from Seq1 import Seq


def print_result(i, sequence,filename):
    print("Gene", filename[16:], ": Most frequent base:", sequence.frequent_base(sequence.count()))


PROJECT_PATH = "../P0/sequences/"
print("-----| Exercise 10 |-----")
s1 = Seq()
filename1 = s1.read_fasta(PROJECT_PATH + "ADA.txt")
print_result("",s1, filename1)

s2 = Seq()
filename2 = s2.read_fasta(PROJECT_PATH + "FRAT1.txt")
print_result("",s2, filename2)

s3 = Seq()
filename3 = s3.read_fasta(PROJECT_PATH + "RNU6_269P.txt")
print_result("",s3, filename3)

s4 = Seq()
filename4 = s4.read_fasta(PROJECT_PATH + "U5.txt")
print_result("",s4, filename4)

s5 = Seq()
filename5 = s5.read_fasta(PROJECT_PATH + "FXN.txt")
print_result("",s5, filename5)