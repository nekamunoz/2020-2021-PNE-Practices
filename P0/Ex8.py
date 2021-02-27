import Seq0

FOLDER = "./sequences/"
ID = "RNU6_269P.txt"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

seq = Seq0.seq_read_fasta(FOLDER + ID)
print("--------| Exercise 8|-------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + ".txt")
    bases_count = Seq0.seq_count(sequence)
    print("Gene", gene + ": Most frequent Base:", Seq0.seq_frequent(bases_count))
