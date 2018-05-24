#coding = utf-8
import socket
class SocketClient:
    def __init__(self):
        self.port=('192.168.94.158',50000)
        self.sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sc.connect(self.port)
        print "connect success"

    def chat_server(self):
        print "chat_server"
        for i in range(100):
            self.sc.sendall("helloworld")
            data = self.sc.recv(1024)
            print "Received "+data
        self.sc.close()

if __name__ == '__main__':
    sc=SocketClient()
    sc.chat_server()

   