import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "0.0.0.0"
port = 777

try:
    server.bind((ip, port))
    server.listen(5)
    print (f"listening in: {ip} : {port} ")
    (client_socket, adress) = server.accept()
    while True:
    print(f"Received from : {adress{0}")
    data = socket_socket.recv(1024)
    print (f"{data}")

    server.close()
except Exception as erro:
    print (f"Erro: `{erro}")