import warnings
from urllib3.exceptions import NotOpenSSLWarning
warnings.simplefilter("ignore", NotOpenSSLWarning)

from flask import Flask, render_template, request, jsonify, session
import paramiko
import os
import base64
import tempfile
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to store connection history in session
active_sessions = {}

def create_ssh_client(host, port, username, password=None, key_file_content=None, passphrase=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if key_file_content:
            try:
                decoded_key = base64.b64decode(key_file_content.encode('utf-8'))
                with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_key:
                    temp_key.write(decoded_key)
                    temp_key_path = temp_key.name
                os.chmod(temp_key_path, 0o600)
                
                with open(temp_key_path, 'rb') as key_file_obj:
                    pkey = paramiko.RSAKey.from_private_key_file(temp_key_path)
                    client.connect(hostname=host, port=port, username=username, pkey=pkey, look_for_keys=False)
            except Exception as e:
                return f'Key Processing Error: {repr(e)}'
        else:
            client.connect(hostname=host, port=port, username=username, password=password)
        return client
    except paramiko.SSHException as e:
        return f'SSH Connection Error: {str(e)}'
    except Exception as e:
        return f'General Connection Error: {repr(e)}'

def handle_terminal_output(client, channel, session_id):
    while True:
        if channel.recv_ready():
            output = channel.recv(1024).decode('utf-8')
            active_sessions[session_id]['output'] += output

@app.route('/')
def index():
    if 'connections' not in session:
        session['connections'] = []
    return render_template('index.html', connections=session.get('connections', []))

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    host = data.get('host')
    port = int(data.get('port', 22))
    auth_type = data.get('auth_type')
    username = data.get('username')
    password = data.get('password') if auth_type == 'password' else None
    key_file_content = data.get('key_file') if auth_type in ['key', 'key+passphrase'] else None
    passphrase = data.get('passphrase') if auth_type == 'key+passphrase' else None
    
    ssh_client = create_ssh_client(host, port, username, password, key_file_content, passphrase)
    
    if isinstance(ssh_client, str):
        return jsonify({'error': ssh_client})
    
    session_id = f"{host}_{username}"
    channel = ssh_client.invoke_shell()
    active_sessions[session_id] = {'client': ssh_client, 'channel': channel, 'output': ''}
    threading.Thread(target=handle_terminal_output, args=(ssh_client, channel, session_id), daemon=True).start()
    
    return jsonify({'status': 'success', 'message': f'Connected to {host} as {username}', 'session_id': session_id})

@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    session_id = data.get('session_id')
    command = data.get('command')
    
    if session_id not in active_sessions:
        return jsonify({'error': 'Invalid session ID'})
    
    channel = active_sessions[session_id]['channel']
    channel.send(command + "\n")
    
    return jsonify({'status': 'success', 'output': active_sessions[session_id]['output']})

@app.route('/get_output', methods=['GET'])
def get_output():
    session_id = request.args.get('session_id')
    if session_id not in active_sessions:
        return jsonify({'error': 'Invalid session ID'})
    
    return jsonify({'status': 'success', 'output': active_sessions[session_id]['output']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)

