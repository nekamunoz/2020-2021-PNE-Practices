def correct_sequence(dna):
    for i in dna:
        if i != "A" and i != "C" and i != "G" and i != "T":
            return False
    return True

def count_bases(dna):
    a, c, g, t = 0, 0, 0, 0
    for i in dna:
        if i == "A":
            a += 1
        elif i == "T":
            t += 1
        elif i == "G":
            g += 1
        elif i == "C":
            c += 1
    return a, c, g, t

dna_sequence = input("Introduce the sequence: ")
if correct_sequence(dna_sequence):
    print("Total length: ", len(dna_sequence))
    a, c, g, t = count_bases(dna_sequence)
    print("A: ", a)
    print("T: ", t)
    print("G: ", g)
    print("C: ", c)
else:
    print("Not a valid dna sequence.")