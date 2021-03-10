class Seq:
    def __init__(self, str_bases):
        if Seq.is_valid_seq2(str_bases):
            self.str_bases = str_bases
            print("New sequence created!")
        else:
            self.str_bases = "ERROR"
            print("INCORRECT Sequence detected.")

    @staticmethod
    def is_valid_seq2(str_bases):
        for i in str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def is_valid_seq(self):
        for i in self.str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def __str__(self):
        return self.str_bases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(s1.is_valid_seq())
print(s2.is_valid_seq())
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

