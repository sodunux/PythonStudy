#coding = utf-8
import socket
class SocketClient:
    def __init__(self):
        pass
    def create_socket(self):
        ''' create an INET,STREAMing Socket '''
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #now connect to the web server on port 80
        #- the normal http port 
        self.s.connect(("www.baidu.com",80))    
    def show_state(self):
        print self.s

if __name__ == '__main__':
    sc=SocketClient()
    sc.create_socket()
    sc.show_state()