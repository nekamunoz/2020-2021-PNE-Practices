from Seq1 import Seq
from client0 import Client

print("-----| Practice 3, Exercise 7 |------")
PORT = 8989
IP = "127.0.0.1"
c = Client(IP, PORT)
print(c)

print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
print(f"GET 0: {c.talk('GET 0')}")
print(f"GET 1: {c.talk('GET 1')}")
print(f"GET 2: {c.talk('GET 2')}")
print(f"GET 3: {c.talk('GET 3')}")
print(f"GET 4: {c.talk('GET 4')}")

print("* Testing INFO...")
print(c.talk('INFO ATTCGATGTGCTAGTCGATGCTGTGTACGTCAGTCAGTCGAT'))
print("* Testing COMP...")
print(c.talk('COMP ATTCGATGTGCTAGTCGATGCTGTGTACGTCAGTCAGTCGAT'))
print("* Testing REV...")
print(c.talk('REV ATTCGATGTGCTAGTCGATGCTGTGTACGTCAGTCAGTCGAT'))

print("* Testing GENE...")
print("GENE U5")
print(c.talk("GENE U5"))
print("GENE ADA")
print(c.talk("GENE ADA"))
print()
print("GENE FRAT1")
print(c.talk("GENE FRAT1"))
print()
print("GENE FXN")
print(c.talk("GENE FXN"))
print()
print("GENE RNU6_269P")
print(c.talk("GENE RNU6_269P"))

