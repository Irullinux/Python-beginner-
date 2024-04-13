from cryptography.fernet import Fernet

def load_key():
    """
    Load the key from the file.
    """
    return open("key.txt", "rb").read()

def encrypt_file(filename, key):
    """
    Encrypt a file using the given key.
    """
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

# Load the key
key = load_key()

# Encrypt a file
encrypt_file("example.txt", key)
