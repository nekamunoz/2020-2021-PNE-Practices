class Seq:
    def __init__(self, str_bases):
        self.str_bases = str_bases

    def __str__(self):
        return self.str_bases

    def valid(self):
        for i in self.str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                self.str_bases = "ERROR"
                return "ERROR!!"
        return "New sequence created!"

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(s1.valid())
print(s2.valid())
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

