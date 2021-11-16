import socket, random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for client
client_color = random.choice(colors)

# server's IP
# if the server is not on this machine, put the private network IP (e.g. 192.168.1.2)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
# we will use this to separate the client name & message
separator_token = "<SEP>"

# initialize TCP socket
s = socket.socket()
print("[*] Connecting to {SH}:{SP}...".format(SH = SERVER_HOST, SP = SERVER_PORT))
# connect to server
s.connect((SERVER_HOST, SERVER_PORT))

# prompt the client for a name
name = input("Enter your name: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make thre thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send = input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break

    # add the datetime, name, & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = "{client_color}[{date_now}] {name}{ST}{to_send}{FS}".format(client_color = client_color, date_now = date_now, name = name, ST = separator_token, to_send = to_send, FS = Fore.RESET)
    # finally, send msg
    s.send(to_send.encode())

# close the socket
s.close()