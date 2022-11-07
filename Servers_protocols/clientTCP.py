import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("142.250.219.206", 80))

client.send("GET / HTTP/1.1\nHost: google.com\n\n")

pacotes_recebidos = client.recv(1024)
print(pacotes_recebidos)