import socket
from threading import Thread


def Send(client):
    while True:
        message = input("-> ")
        message = message.encode("utf-8")

        client.send(message)


def reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode("utf-8")

        print(requete_client)

        # perte de connexion
        if not requete_client:
            print("fin de la conversation")
            break



Host = "192.168.0.29"
Port = 8000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((Host, Port))
socket.listen(1)

# on attend une connexion
client, ip = socket.accept()
print(f"le client d'ip {ip} s'est connecté")


envoi = Thread(target=Send, args=[client])
recep = Thread(target = reception, args=[client])

envoi.start()
recep.start()

recep.join()


client.close()
socket.close()