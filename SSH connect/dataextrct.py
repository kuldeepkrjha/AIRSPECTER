import os
import paramiko

def copy_file_from_remote(remote_path, local_path, hostname, port, private_key_path):
    key = paramiko.RSAKey(filename=private_key_path)

    transport = paramiko.Transport((hostname, port))
    transport.connect(username="YOUR_SSH_USERNAME", pkey=key)

    sftp = paramiko.SFTPClient.from_transport(transport)
    remote_file_path = os.path.join(remote_path)
    local_file_path = os.path.join(local_path, os.path.basename(remote_path))
    sftp.get(remote_file_path, local_file_path)

    sftp.close()
    transport.close()
    print(f"File '{os.path.basename(remote_path)}' copied from remote system to local system.")

if __name__ == "__main__":
    remote_path = input("Enter the remote file or directory path to copy: ")
    local_path = input("Enter the local directory path to save the file or directory: ")
    hostname = "localhost"  # Assuming ngrok is forwarding to localhost
    port = 12345  # Replace with the actual port ngrok is forwarding
    private_key_path = "path/to/your/private/key"  # Replace with the actual path to your private key

    copy_file_from_remote(remote_path, local_path, hostname, port, private_key_path)
    print("File or directory copied from remote system to local system.")
