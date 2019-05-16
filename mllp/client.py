import socket

from hl7apy.parser import parse_message

def send_message(host, port , msg):
    # establish the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(parse_message(msg).to_mllp().encode('UTF-8'))
        # receive the answer
        received = sock.recv(1024*1024)
        return received
    finally:
        sock.close()


if __name__ == '__main__':
    msg = \
        'MSH|^~\&|REC APP|REC FAC|SEND APP|SEND FAC|20110708163513||QBP^Q22^QBP_Q21|111069|D|2.5|||||ITA||EN\r' \
        'QPD|IHE PDQ Query|111069|@PID.5.2^SMITH||||\r' \
        'RCP|I|'

    res = send_message('localhost', 2575 , msg)
    print(res)
    print("Received response: ")
    print(repr(res))