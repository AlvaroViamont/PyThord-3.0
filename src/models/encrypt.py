from cryptography.fernet import Fernet

def encrypt(message: str) -> bytes:
    key = Fernet.generate_key()
    return key, Fernet(key).encrypt(message.encode())

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def remov_string_b (text: str) -> str:
    return text[2: -1]