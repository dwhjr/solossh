import paramiko
import os

key_path = os.path.expanduser("~/Pem/LightsailDefaultKey-us-east-1.pem")

try:
    pkey = paramiko.RSAKey(filename=key_path)
    print("✅ Key loaded successfully!")
except paramiko.PasswordRequiredException:
    print("❌ The private key file is encrypted!")
except paramiko.SSHException as e:
    print(f"❌ SSH Key Error: {e}")
except FileNotFoundError:
    print("❌ The key file does not exist. Check the path.")

