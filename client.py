import socket
from threading import Thread


def Send(socket):
    while True:
        message = input("-> ")
        message = message.encode('utf-8')
        socket.send(message)


def reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")
        print(requete_server)


Host = "192.168.0.29"
Port = 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))


envoi = Thread(target=Send, args=[socket])
recep = Thread(target=reception, args=[socket])

envoi.start()
recep.start()