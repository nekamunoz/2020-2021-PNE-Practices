class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases

    def __str__(self):
        return self.str_bases

    def len(self):
        return len(self.str_bases)

def generate_seqs(pattern, number):
    new_seq = []
    for e in range(0, number):
        seq = new_seq.append(pattern)
        seq_info = Seq(seq)
        print(f"Sequence {e}: (Length: {seq_info.len()}) {seq}")
    return new_seq

def print_seqs(seq):
    str_seq = ""
    for i in seq:
        str_seq += i
    return str_seq

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
for i in seq_list1:
    print(print_seqs(seq_list1[i]))
print("List 2:")
for e in seq_list2:
    print(print_seqs(seq_list2[e]))