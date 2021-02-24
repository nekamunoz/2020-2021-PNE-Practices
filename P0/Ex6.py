import Seq0

FOLDER = "./sequences/"
ID = "RNU6_269P.txt"

seq = Seq0.seq_read_fasta(FOLDER + ID)
print("Gene", ID, ":")
print("Frag: ", seq[3:40])
print("Rever: ", Seq0.seq_reverse(seq[3:40]))