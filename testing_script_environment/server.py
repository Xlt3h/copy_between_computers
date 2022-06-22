import socket


s = socket.socket
host = ''
port = 7777  # arbitrary non-privileged port
s.bind((host, port))
s.listen(2)
print("listening for incoming connection on port:", port)
conn_1, addr_1 = s.accept()
conn_2, addr_2 = s.accept()
running = True
try:
    while True:
        recv_comp_1 = conn_1.recv(1024)
        recv_comp_2 = conn_2.recv(1024)
        if recv_comp_1:
            pass
        if recv_comp_2:
            pass
except:
    print("one of the pc has been disconnected")
    conn_1.close()
    conn_2.close()
    s.close()