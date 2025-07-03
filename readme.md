# Project Setup Guide: MongoDB & Neo4j Installation

Follow the steps below to install and configure **MongoDB** and **Neo4j** on your machine.

---

## 1. Install MongoDB

### Windows

1. Download MongoDB from the official website:  
   👉 https://www.mongodb.com/try/download/community
2. Follow the installer instructions.
3. After installation, open **Command Prompt** and run:
   ```bash
   mongod
   ```

### MacOS

1. Install using Homebrew (In case you have yet to download: https://brew.sh/)
   brew tap mongodb/brew
   brew install mongodb-community@7.0
2. Start the service
   brew services start mongodb/brew/mongodb-community
3. Verify if it's running
   mongosh

### Linux

a. Arch Linux 1. Install via pacman:
sudo pacman -S mongodb-community
(In case your using yay):
yay -S mongodb-community 2. Start and enable the service
sudo systemctl start mongodb
sudo systemctl enable mongodb
b. Ubuntu 1. Import public key Import the public key and add MongoDB to the sources list
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list 2. Update and install
sudo apt update
sudo apt install -y mongodb-org 3. Start and verify
sudo systemctl start mongod
sudo systemctl enable mongod

## For env

'
pip install dotenv
'
