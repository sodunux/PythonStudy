#coding = utf-8
import socket
class SocketClient:
    def __init__(self):
        self.addr=('localhost',8080)
        self.sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sc.connect(self.addr)
        print "connect success"
    def chat_server(self):
        print "chat_server"
        for i in range(100):
            self.sc.sendall("helloworld")
            data = sc.recv(1024)
            print "Received"+data
        s.close()

 
    def show_state(self):
        print self.s

if __name__ == '__main__':
    sc=SocketClient()
    sc.chat_server()

   