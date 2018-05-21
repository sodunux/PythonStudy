#coding = utf-8
import socket
class SocketServer:
    def __init__(self):
        self.ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ss_port=(socket.gethostname(),8001)
        self.ss.bind(self.ss_port)
        self.ss.listen(5)
    def __del__(self):
        

    def chat_client(self):
        self.conn_addr=self.ss.accept()

    def show_state(self):
        print self.ss
        print socket.gethostname()
        #while 1:
        #   print self.conn_addr
        #print socket.SocketType(self.s)


if __name__ == '__main__':
    ss=SocketServer()
    ss.create_socket()
    ss.chat_client()
    ss.show_state()


