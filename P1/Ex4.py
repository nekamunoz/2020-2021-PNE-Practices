from Seq1 import Seq

print("-----| Exercise 4 |-----")
seq0 = Seq()
seq1 = Seq("AGTA")
seq2 = Seq("Invalid sequence")
print()
print("Sequence " + str(0) + " (Length: " + str(seq0.len()) + "): " + str(seq0))
print("Sequence " + str(1) + " (Length: " + str(seq1.len()) + "): " + str(seq1))
print("Sequence " + str(2) + " (Length: " + str(seq2.len()) + "): " + str(seq2))