import socket

from hl7apy.parser import parse_message

def send_message(host, port , msg):
    # establish the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(msg.to_mllp().encode('UTF-8'))

        # receive the answer
        received = sock.recv(1024*1024)
        return received
    finally:
        sock.close()
