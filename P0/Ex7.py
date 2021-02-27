import Seq0

FOLDER = "./sequences/"
ID = "RNU6_269P.txt"

seq = Seq0.seq_read_fasta(FOLDER + ID)
print("--------| Exercise 7|-------")
print("Gene", ID[0:-4] + ":")
print("Frag: ", seq[0:20])
print("Comp: ", Seq0.seq_complement(seq[0:20]))