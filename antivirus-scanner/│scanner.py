import os
import yara
import hashlib
import requests

# ===============================
# CONFIGURATION
# ===============================

YARA_RULE_FILE = "malware_rules.yar"
VIRUSTOTAL_API_KEY = "PASTE_YOUR_VIRUSTOTAL_API_KEY_HERE"
VT_URL = "https://www.virustotal.com/api/v3/files/"

# ===============================
# LOAD YARA RULES
# ===============================

def load_rules():
    try:
        rules = yara.compile(filepath=YARA_RULE_FILE)
        print("[+] YARA rules loaded")
        return rules
    except Exception as e:
        print("Error loading YARA:", e)
        return None

# ===============================
# CALCULATE SHA256
# ===============================

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

# ===============================
# CHECK VIRUSTOTAL
# ===============================

def check_virustotal(file_hash):
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(VT_URL + file_hash, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        return stats["malicious"], stats["suspicious"]
    else:
        return None

# ===============================
# SCAN FILE
# ===============================

def scan_file(file_path, rules):
    print(f"\nScanning: {file_path}")

    # YARA Scan
    try:
        matches = rules.match(file_path)
        if matches:
            print("⚠ YARA MATCH FOUND:")
            for match in matches:
                print(" - Rule:", match.rule)
    except:
        pass

    # Hash
    file_hash = calculate_hash(file_path)
    if file_hash:
        print("SHA256:", file_hash)

        # VirusTotal
        if VIRUSTOTAL_API_KEY != "PASTE_YOUR_VIRUSTOTAL_API_KEY_HERE":
            result = check_virustotal(file_hash)
            if result:
                malicious, suspicious = result
                print(f"VirusTotal → Malicious: {malicious}, Suspicious: {suspicious}")
                if malicious > 0:
                    print("🚨 FILE DETECTED AS MALICIOUS")

# ===============================
# SCAN DIRECTORY
# ===============================

def scan_directory(directory):
    rules = load_rules()
    if not rules:
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path, rules)

# ===============================
# MAIN
# ===============================

if __name__ == "__main__":
    path = input("Enter folder path to scan: ")

    if os.path.exists(path):
        scan_directory(path)
    else:
        print("Invalid path")
