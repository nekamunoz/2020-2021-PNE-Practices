import termcolor
from Seq0 import Seq, generate_seqs

seq_lis1 = generate_seqs("A", 3)
seq_lis2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'yellow')
Seq.print_seqs(seq_lis1)
termcolor.cprint("List 2:", 'green')
Seq.print_seqs(seq_lis2)
