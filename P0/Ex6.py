import Seq0

FOLDER = "./sequences/"
ID = "RNU6_269P.txt"

seq = Seq0.seq_read_fasta(FOLDER + ID)

print("--------| Exercise 6|-------")
print("Gene", ID[0:-4] + ":")
print("Frag: ", seq[3:40])
print("Rever: ", Seq0.seq_reverse(seq[3:40]))