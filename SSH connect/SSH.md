## Remote Access via SSH Connection

SSH (Secure Shell) is a cryptographic network protocol that allows secure and encrypted communication between two devices over an unsecured network. It is commonly used for remote access to servers and devices, providing a secure way to log in and execute commands remotely.

### How SSH Works

1. **Server Setup:** The remote device (server) needs to have an SSH server installed and running to accept incoming SSH connections. Typically, this is OpenSSH on Unix-like systems.

2. **Client Connection:** On the local device (client), you use an SSH client (e.g., OpenSSH client on Unix-like systems or PuTTY on Windows) to initiate a connection to the remote server.

3. **Authentication:** Once the connection is established, the client and server engage in an authentication process. This usually involves the client providing valid credentials, such as a username and password or SSH key pair.

4. **Encryption:** After successful authentication, all data transferred between the client and server is encrypted, ensuring that sensitive information remains secure during the session.

### Establishing an SSH Connection

To connect to a remote server via SSH, use the following command in the terminal or command prompt:

```bash
ssh username@remote_server_ip

####For key based secured authentication

'''bash
ssh -i /path/to/private_key username@remote_server_ip
