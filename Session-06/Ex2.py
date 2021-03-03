class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases

    def __str__(self):
        return self.str_bases

    def len(self):
        return len(self.str_bases)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for s in range(0, len(seq_list)):
    print(f"Sequence {s} (Length: {seq_list[s].len()}): {seq_list[s]}")