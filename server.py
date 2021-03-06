import socket
from threading import Thread

# server's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
# use this to separate the client name and message
separator_token = "<SEP>"

# initilialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as resuable as possible
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    # this func keep listening for a message from 'cs' socket
    # whenever a message is received, broadcast it to all other connected clients

    while True:
        try:
            # keep listening for a message from 'cs' socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove from set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a msg, replace the <SEP> token with ": " for nice printing
            msg = msg.replace(separator_token, ": ")
        
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())

while True:
    # keep listening for new connections
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected...")
    # add the new connected client to the connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's msgs
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()