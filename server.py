""".

This server code simply accepts a client request, returns the string 'Hello
world' and prints the address of the client
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 10000

sock.bind((host, port))

sock.listen(5)

while True:
    clientsock, addr = sock.accept()
    print("Got a connection from %s" %str(addr))
    msg = "Hello world" + "\r\n"
    clientsock.send(msg.encode('ascii'))
    clientsock.close()
