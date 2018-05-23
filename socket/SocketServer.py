#coding = utf-8
import socket
class SocketServer:
    def __init__(self):
        self.ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ss_port=('localhost',8080)
        self.ss.bind(self.ss_port)
        self.ss.listen(5)
    def __del__(self):
        pass

    def chat_client(self):
        conn,addr = self.ss.accept()
        print "Connected by "+addr()
        while 1:
            data = conn.recv(1024)
            if data<=0:
                break
            else:
                conn.sendall(data)
            conn.close()

    def show_state(self):
        print self.ss
        print socket.gethostname()
        #while 1:
        #   print self.conn_addr
        #print socket.SocketType(self.s)


if __name__ == '__main__':
    ss=SocketServer()
    ss.chat_client()
    #ss.show_state()


