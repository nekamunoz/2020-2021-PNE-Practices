from client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {2}, Exercise {4} |------")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")