import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5051        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # while(1):
    #     sendData=input('Enter the terminal code: ')
    #     s.sendall(sendData.encode())
    #     data = s.recv(1024)
    #     if not data:
    #         s.close()
    #     if(data.decode()=="stop"):
    #         s.close()
    #     print('Received', repr(data))
    with open('received_file.png','wb') as f:
        print('file opened')
        
        while(1):
            data=s.recv(1024)
            print("data",data)
            if not data:
                break
            else:
                f.write(data)
        

    
