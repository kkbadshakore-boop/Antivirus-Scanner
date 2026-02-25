
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


🔍 How It Works
Loads YARA rules
Scans each file in selected directory
Matches binary patterns against malware signatures
Generates SHA256 hash
Checks file hash with VirusTotal
Displays detection results



🐉 Installation (Kali Linux)

1️⃣ Update System

sudo apt update && sudo apt upgrade -y



2️⃣ Install Required Tools

sudo apt install python3 python3-pip yara -y


3️⃣ Clone Repository

git clone https://github.com/kkbadshakore-boop/Antivirus-Scanner.git
cd antivirus-scanner


4️⃣ Install Python Dependencies

pip3 install -r requirements.txt --break-system-packages


5️⃣ Add VirusTotal API Key

Create account on VirusTotal
Get your API key
Open scanner.py
Replace:
VIRUSTOTAL_API_KEY = "PASTE_YOUR_VIRUSTOTAL_API_KEY_HERE"
with your real API key.

▶ Run Scanner

python3 scanner.py
