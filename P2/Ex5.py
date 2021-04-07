from client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {2}, Exercise {5} |------")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
print(c.debug_talk("Sending the U5 Gene to the server..."))
print()
print(c.debug_talk(Path("U5.txt").read_text()))