import socket

#host
host = ''

#port
port  = 7777

s = socket.socket()

#bind for connection
s.bind((host,port))

#listen to 2 devices
s.listen(2)

print("listening for incoming connection on port:", port)

#accept incoming connections

#for connection one
conn_1,addr_1 = s.accept()

#for connection two
conn_2,addr_2 = s.accept()

#running
running = True
try:
    while running:
        #receive data from connection one
        data_1 = conn_1.recv(1024)

        #receive data from connection two
        data_2 = conn_2.recv(1024)

        #if data_1 is not empty
        if data_1:
            #send data_1 to connection two
            conn_2.send(data_1)

        #if data_2 is not empty
        if data_2:
            #send data_2 to connection one
            conn_1.send(data_2)
except ConnectionResetError:
    print("one of the pc has been disconnected")