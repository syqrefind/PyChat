from socket import *

HOST = '192.168.1.116'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
try:
    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(bytes(data,'utf-8'))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8')) 

    tcpCliSock.close()
except KeyboardInterrupt as e:
    print('\nDisconnected from the server.')
