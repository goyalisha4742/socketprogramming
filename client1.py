""".

This is the client code for server1.py
"""

import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port))
    message = raw_input("-> ")
    while message != 'q':
        sock.send(message)
        data = sock.recv(1024)
        print "Recieved from server: " + str(data)
        message = raw_input("-> ")
    sock.close()

if __name__ == '__main__':
    Main()
