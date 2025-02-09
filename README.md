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

## Deploy with Docker
```bash
docker-compose up -d
```
Then, open:  
🔗 `http://localhost:5000`

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


