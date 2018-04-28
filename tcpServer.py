import socket,sys,_thread

clients=[]

def recvdata(s):
    global clients
    flag=[]
    data=s.recv(1024)
    while data:
        for i in clients:
            # whether send back to self
            toself=True
            if (i != s) or toself:
                try:
                    i.send(data)
                except:
                    flag.append(i)
                    continue
            if len(flag):
                for i in flag:
                    print("Disconnected : %s" % str(i.getpeername()))
                    clients.remove(i)
                flag=[]
        data=s.recv(1024)
            
def main():
    port=23333  # port
    cnum=5      # max number of clients
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),port))
    s.listen(cnum)
    print("Waiting For Connections")
    while True:
        clientsocket,clientaddress=s.accept()
        clients.append(clientsocket)# add the new client to the list
        _thread.start_new_thread(recvdata,(clientsocket,))
        print("Connected    : %s" % str(clientaddress))

if __name__=="__main__":
    main()
