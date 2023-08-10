import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_directory(directory_path, encryption_key):
    # Generate a random salt
    salt = os.urandom(16)

    # Derive key from the encryption key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(encryption_key.encode())

    # Encrypt and write the salt to the encrypted file
    with open("salt.bin", "wb") as salt_file:
        salt_file.write(salt)

    # Encrypt each file in the directory
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        encrypted_filepath = os.path.join("encrypted", filename + ".enc")

        with open(filepath, "rb") as input_file, open(encrypted_filepath, "wb") as output_file:
            plaintext = input_file.read()
            cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()
            output_file.write(ciphertext)

    print("Directory encrypted.")

def generate_decryption_script():
    with open("decryption_script.py", "w") as script_file:
        script_file.write("""\
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Prompt user for decryption key securely
decryption_key = input("Enter decryption key: ")

# Read the salt from the file
with open("salt.bin", "rb") as salt_file:
    salt = salt_file.read()

# Derive key from the decryption key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    iterations=100000,
    salt=salt,
    length=32,
    backend=default_backend()
)
key = kdf.derive(decryption_key.encode())

# Decrypt each encrypted file
for filename in os.listdir("encrypted"):
    if filename.endswith(".enc"):
        encrypted_filepath = os.path.join("encrypted", filename)
        decrypted_filepath = os.path.join("decrypted", filename[:-4])

        with open(encrypted_filepath, "rb") as input_file, open(decrypted_filepath, "wb") as output_file:
            ciphertext = input_file.read()
            cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            output_file.write(plaintext)

print("Directory decrypted and ready to use.")
""")
    print("Decryption script generated.")

def remove_log_files(log_dir):
    for root, dirs, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
    print("Log files removed.")


if __name__ == "__main__":
    print("Choose an action:")
    print("1. Encrypt the directory")
    print("2. Remove log files")
    print("3. Encrypt the directory and remove log files")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1" or choice == "3":
        directory_path = input("Enter the directory path to encrypt: ")
        encryption_key = input("Enter encryption key: ")

        if not os.path.exists("encrypted"):
            os.makedirs("encrypted")

        if not os.path.exists("decrypted"):
            os.makedirs("decrypted")

        encrypt_directory(directory_path, encryption_key)
        generate_decryption_script()
        print("Directory encrypted.")

    if choice == "2" or choice == "3":
        log_dir = input("Enter the directory path to remove log files from: ")
        remove_log_files(log_dir)
        print("Log files removed.")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
