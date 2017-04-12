import socket,sys,os,_thread

clients=[]

def handledata(s):
    global clients
    data=s.recv(1024)
    while data:
        try:
            for i in clients:
                # 转发是否包括自己
                if i != s:
                    i.send(data)
            data=s.recv(1024)
        except:
            sys.exit(0)
            
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),2333))# 端口
    s.listen(5)# 最大连接数
    print("Waiting For Connections")
    while True:
        clientsocket,clientaddress=s.accept();
        clients.append(clientsocket)#新连接加入转发客户端列表
        _thread.start_new_thread(handledata,(clientsocket,))
        print("Connected : %s" % str(clientaddress))

if __name__=="__main__":
    main()