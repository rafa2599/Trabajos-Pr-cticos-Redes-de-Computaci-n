import socket
import json

HOST = "127.0.0.1"
PORT = 5000

message = {
    "group": "WAN PIECE",
    "payload": "Hello World"
}


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(json.dumps(message).encode("utf-8"))

client.close()
