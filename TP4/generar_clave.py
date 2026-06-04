from cryptography.fernet import Fernet
clave = Fernet.generate_key()
with open("clave.key", "wb") as key_file:
    key_file.write(clave)
print("Clave generada y guardada en 'clave.key'")

