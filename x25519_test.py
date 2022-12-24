from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization



server_private_key = X25519PrivateKey.generate()
server_private_key = X25519PrivateKey.from_private_bytes(bytearray.fromhex("909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"))

server_public_key = server_private_key.public_key()
server_public_key_hex = server_public_key.public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw).hex()

print(server_public_key_hex)




