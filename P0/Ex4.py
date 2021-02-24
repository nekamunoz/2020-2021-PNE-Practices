import Seq0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "G", "T"]

print("--------| Exercise 4|-------")

for gene in gene_list:
    print("Gene", gene + ":")
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))