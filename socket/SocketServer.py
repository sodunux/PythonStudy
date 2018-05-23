#coding = utf-8
import socket
class SocketServer:
    def __init__(self):
        self.ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ss_port=('192.168.1.7',8080)
        self.ss.bind(self.ss_port)
        self.ss.listen(5)

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

if __name__ == '__main__':
    ss=SocketServer()
    ss.chat_client()



