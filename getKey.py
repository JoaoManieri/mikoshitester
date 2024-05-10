from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def getKey():
    senha = b"protecno"
    with open("chave_privada.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=senha,
            backend=default_backend()
        )
        return private_key
