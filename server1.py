""".

This server code uses TCP connection and just returns
the capitalized version of the text recieved from the
client
"""

import socket


def Main():

    host = '127.0.0.1'
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))

    sock.listen(1)
    c, addr = sock.accept()
    print "Conncection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()
