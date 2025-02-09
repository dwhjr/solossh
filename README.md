# SOLOSSH
**A Web-Based SSH Client for Secure Remote Access**  

SOLOSSH is a **Flask-based web SSH client** that allows users to securely connect to remote servers through their browser. It provides a lightweight and efficient way to manage SSH sessions without requiring a dedicated client.

---

## 🔧 Features
- 🌐 **Web-based SSH** – Access your servers from any browser  
- 🔒 **Secure authentication** – Supports SSH key authentication  
- ⚡ **Real-time terminal** – Responsive and lightweight interface  
- 🐳 **Docker support** – Easily deployable with Docker  
- 🎨 **Customizable UI** – Themed to match `solosftp.solo-orbit.com`  
- 📡 **SocketIO integration** – For real-time SSH communication  

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/dwhjr/solossh.git
cd solossh
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```
Access the app at:  
🔗 `http://localhost:5000`

---

## Requirements
```
flask
paramiko
docker
urllib3
```

---

## NGINX Conf
```
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    sendfile on;
    keepalive_timeout 65;

    server {
        listen 80;
        server_name _;

        location / {
            proxy_pass http://127.0.0.1:5003; # Flask/Django/Python app running inside the container
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

## Docker

## Dockerfile
```
FROM python:3.11

WORKDIR /app

# Install system dependencies including NGINX
RUN apt-get update && apt-get install -y \
    nginx \
    bash \
    libssl-dev \
    libffi-dev \
    build-essential \
    python3-dev \
    python3-pip \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for web access
EXPOSE 80

# Start NGINX and the Python app
ENTRYPOINT ["bash", "-c", "service nginx start && python3 /app/app.py"]
```

## docker-compose.yml
```
services:
  solossh:
    build: ../solossh
    image: solossh-img
    container_name: solossh
    restart: unless-stopped
    ports:
      - "5003:80"
    volumes:
      - ../solossh:/app
    command: python3 /app.py
```

## Deploy with Docker
```bash
docker-compose up -d
```
Then, open:  
🔗 `http://localhost:5000`

---
## Static Tree Structure
```bash
.
├── css
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── ## bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
├── js
│   ├── bootstrap.bundle.js
│   ├── bootstrap.bundle.js.map
│   ├── bootstrap.bundle.min.js
│   ├── bootstrap.bundle.min.js.map
│   ├── bootstrap.esm.js
│   ├── bootstrap.esm.js.map
│   ├── bootstrap.esm.min.js
│   ├── bootstrap.esm.min.js.map
│   ├── bootstrap.js
│   ├── bootstrap.js.map
│   ├── bootstrap.min.js
│   └── bootstrap.min.js.map
└── xterm
    ├── xterm.css
    ├── xterm.js
    └── xterm.js.map
```

---

## Configuration
Modify **`config/settings.py`** to update:
- SSH Server settings  
- Authentication options  
- UI preferences  

---

## Security Best Practices
- Use **SSH key authentication** for better security.  
- Configure a **reverse proxy** like Nginx for HTTPS.  
- Limit access via **firewall rules** if exposed publicly.  

---

## License
This project is licensed under the **MIT License**.  

---

## Structure
```bash
.
├── CSS
│   └── bootstrap-5.3.3-dist
├── Dockerfile
├── Libs
│   ├── node_modules
│   ├── package-lock.json
│   └── package.json
├── __pycache__
│   └── app.cpython-312.pyc
├── app.py
├── docker-compose.yml
├── keytest.py
├── nginx.conf
├── python
├── requirements.txt
├── solossh
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── static
│   ├── css
│   ├── js
│   └── xterm
└── templates
    └── index.html
```

## Contact
For issues or feature requests, create a GitHub **Issue** or reach out to:  
[service@solo-orbit.com]


