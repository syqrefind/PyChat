#-*-encoding:utf-8-*-
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

try:
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print ('等待客户端连接...')
        tcpCliSock, addr = tcpSerSock.accept()
        print ('...连接自:'), addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' %(bytes(ctime()), data))

        tcpCliSock.close()
    tcpSerSock.close()
except KeyboardInterrupt as e:
    print('\n服务器终止.')
