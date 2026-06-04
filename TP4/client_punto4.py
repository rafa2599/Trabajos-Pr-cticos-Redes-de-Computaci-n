import socket
import json
from cryptography.fernet import Fernet

# clave generada
with open("clave.key", "rb") as key_file:
    clave = key_file.read()
cipher = Fernet(clave)


message = {
    "group": "WAN PIECE",
    "payload": "Hello World"
}
texto_a_cifrar = message["payload"].encode("utf-8")
message["payload"] = cipher.encrypt(texto_a_cifrar).decode("utf-8")



HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(json.dumps(message).encode("utf-8"))

client.close()


