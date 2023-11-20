import os
import paramiko

def establishSshConnection(hostname, username, privateKeyPath, maxRetries=3, retryDelay=5):
    retries = 0
    while retries < maxRetries:
        try:
            client.connect(hostname, username=username, key_filename=privateKeyPath)
            print("SSH connection established successfully!")
            return True
        except paramiko.SSHException as e:
            print(f"Error establishing SSH connection: {e}")
            print(f"Retrying in {retryDelay} seconds...")
            retries += 1
            time.sleep(retryDelay)
    print("Failed to establish SSH connection after retries.")
    return False

def listRemoteFiles(remotePath, sftp):
    try:
        files = sftp.listdir(remotePath)
        print(f"Files in remote directory '{remotePath}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Remote directory '{remotePath}' not found.")
    except Exception as e:
        print(f"Error listing files: {e}")

# Remote machine details
hostname = '192.168.1.34'
username = 'astroberry'
remotePath = '/home/astroberry/git'

# Create a Paramiko SSH client
client = paramiko.SSHClient()
client.load_system_host_keys()  # Load system host keys
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto-add new hosts

# Connect to the remote machine using your private key
privateKeyPath = 'C:\\Users\\robst\\.ssh\\id_rsa'
#privateKeyPath = '/home/astroberry/.ssh/id_ed2559'

if establishSshConnection(hostname, username, privateKeyPath):
    try:
        # Create a transport object for SFTP (Secure File Transfer Protocol)
        sftp = client.open_sftp()

        # List files in the remote directory
        listRemoteFiles(remotePath, sftp)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SFTP session and SSH connection
        sftp.close()
        client.close()
else:
    print("Aborting script due to SSH connection issues.")
