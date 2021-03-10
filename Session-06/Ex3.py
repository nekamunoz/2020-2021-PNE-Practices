from Seq0 import Seq, generate_seqs

seq_lis1 = generate_seqs("A", 3)
seq_lis2 = generate_seqs("AC", 5)

print("List 1:")
Seq.print_seqs(seq_lis1)
print("List 2:")
Seq.print_seqs(seq_lis2)