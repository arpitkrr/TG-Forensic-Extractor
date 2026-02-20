# TG-Forensic-Extractor

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram Logo" width="100"/>
</p>

<h1 align="center">TG-Forensic-Extractor</h1>

<p align="center">
  <strong>A specialized OSINT & Forensic Analysis Tool for mapping Command & Control (C2) infrastructure from compromised Telegram Bot Tokens.</strong>
</p>

---

### 🛡️ Overview

**TG-Forensic-Extractor** is a Python-based utility designed for Threat Intelligence Analysts and Digital Forensic Investigators. It automates the extraction of critical metadata, actor identities, and C2 routing information when a malicious Telegram Bot Token is recovered (e.g., from a phishing kit or malware payload).

By querying the Telegram API, this tool bypasses the need for complex API routing, instantly revealing the infrastructure behind a threat actor's operation.

### ✨ Core Features

* **Bot Identity Extraction:** Instantly retrieves the Bot's Username, First Name, and internal ID.
* **Auto-Detection:** Automatically detects the target Chat ID from recent malicious traffic logs (Update Queue).
* **Target Profiling:** Extracts the Group/Channel name, description, and type (Supergroup, Channel, etc.).
* **Administrator Mapping:** If privileges allow, extracts a list of Group Administrators and active members.
* **Payload Interception:** Retrieves the last intercepted message payload or media type sitting in the bot's queue.

### 🚀 Installation

Ensure you have Python 3 installed. Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/ArpitKumar/TG-Forensic-Extractor.git](https://github.com/ArpitKumar/TG-Forensic-Extractor.git)
cd TG-Forensic-Extractor
pip install requests
