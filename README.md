# Python Antivirus Scanner

## Project Goal
Build a simple signature-based antivirus scanner using:

- Python
- YARA Rules
- VirusTotal API

## Features
- Binary signature detection using YARA
- SHA256 file hashing
- VirusTotal threat intelligence check
- Recursive directory scanning

🐉 How to Run in Kali Linux
1️⃣ Update System

Open terminal and run:

sudo apt update && sudo apt upgrade -y


2️⃣ Install Python (if not installed)

Kali usually has Python3 preinstalled. Check:

python3 --version

If not installed:

sudo apt install python3 python3-pip -y

3️⃣ Install YARA

sudo apt install yara -y

Verify: yara --version

4️⃣ Clone Your GitHub Project

git clone https://github.com/yourusername/antivirus-scanner.git
cd antivirus-scanner

5️⃣ Install Python Requirements
pip3 install -r requirements.txt

If pip3 gives permission error:

pip3 install -r requirements.txt --break-system-packages
