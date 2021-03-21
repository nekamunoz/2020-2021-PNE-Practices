from client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {2}, Exercise {3} |------")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

print("Sending a message to the server...")
response = c.talk("Yes, this is working yuhuuuuu!!!")
print(response)