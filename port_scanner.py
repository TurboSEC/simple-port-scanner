import socket


ip = "127.0.0.1" 

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.connect((ip,port))
        sock.settimeout(0.1)
        sock.connect((ip, port))
        sock.close() # Good practice to close the socket
        return True
    except:
        return False

for port in range(1, 1024):
    result = scan(port)
    if result:
        print(f"Port {port} is open!")
    else:
         print(f"Port {port} is closed!")