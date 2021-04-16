from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {2}, Exercise {6} |------")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

s = Seq()
s.read_fasta('../Session-04/FRAT1.txt')
i = 0
count = 0
while i < len(s.str_bases) and count < 5:
    fragment = s.str_bases[i:i+10]
    count += 1
    i += 10
    fragment_text = "Fragment " + str(count) + ":" + fragment
    print(fragment_text)
    print(c.debug_talk(fragment_text))