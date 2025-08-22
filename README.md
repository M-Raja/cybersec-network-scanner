# Network Vulnerability Scanner

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg?style=for-the-badge)

<br>
<br>

<img   align="center" alt="Coding" width="500" height="300" src="https://github.com/user-attachments/assets/ce6e29d7-7c6e-41e9-a121-7cc1e413c261">


<br>
<br>

**A comprehensive network port scanner and vulnerability assessment tool built in Python for educational penetration testing.**

 [Documentation](docs/setup_and_usage.md) • [Safety](#safety-features) 

</div>



## ⚠️ **CRITICAL DISCLAIMER**

<div align="center">

**This tool is for EDUCATIONAL PURPOSES ONLY!**

</div>

- Only scan networks and systems you **OWN** or have **EXPLICIT PERMISSION** to test
- Unauthorized scanning is **ILLEGAL** in most jurisdictions
- Use responsibly and ethically
- You are responsible for ensuring proper authorization



## Project Overview

This scanner helps you learn:
- **Network reconnaissance** techniques
- **Port scanning** methodologies  
- **Service identification** and banner grabbing
- **Ethical hacking** fundamentals
- **Vulnerability assessment** basics



### System Requirements
- Kali Linux VM (recommended) or any Linux distribution
- Python 3.6+
- Network connectivity
- Administrative privileges (for some features)

<br>

### GitHub Repository Structure

```bash

network-vulnerability-scanner/
│── simple_scanner.py          # Your source code
│── README.md                  # Professional showcase doc
│── docs/
│    └── setup_and_usage.md    # Full setup guide (your docs)
│── LICENSE                    # (MIT or Apache 2.0 recommended)
│── .gitignore

```

<br>


### Virtual Environment Installation

### 📥 Download & Setup

🔹 Option 1: Clone with Git (recommended)

```bash

# Clone the repository from GitHub

> git clone https://github.com/M-Raja/cybersec-network-scanner

# Move into the project folder

> cd cybersec-network-scanner

```

🔹 Option 2: Download ZIP (no Git required)

```bash

# Step 1: Open your browser and go to:

 https://github.com/M-Raja/cybersec-network-scanner

# Step 2: Click on the green "Code" button → then click "Download ZIP"

# Step 3: Extract the ZIP file to your desired folder

# Step 4: Open a terminal or command prompt inside the extracted folder

> cd cybersec-network-scanner   # (folder name after extracting ZIP)

```
<br>

> **📖 For detailed setup instructions, see [Setup and Usage Guide](docs/setup_and_usage.md)**




## Basic Usage

1. **Start the Scanner**
   ```bash
   python simple_scanner.py
   ```

2. **Follow the Prompts**
   - Enter target IP address when prompted
   - Choose scan type (1-3)
   - Wait for scan completion

## What to Look For

### Common Open Ports & Services

| Port | Service | Description | Security Risk | Status |
|------|---------|-------------|---------------|--------|
| 21 | FTP | File Transfer Protocol | **High** (unencrypted) | ⚠️ |
| 22 | SSH | Secure Shell | **Low** (if configured properly) | ✅ |
| 23 | Telnet | Remote Login | **High** (unencrypted) | ⚠️ |
| 25 | SMTP | Email Server | **Medium** | ⚠️ |
| 53 | DNS | Domain Name System | **Low** | ✅ |
| 80 | HTTP | Web Server | **Medium** | ⚠️ |
| 135 | RPC | Remote Procedure Call | **High** | ⚠️ |
| 139 | NetBIOS | Windows Networking | **High** | ⚠️ |
| 443 | HTTPS | Secure Web Server | **Low** | ✅ |
| 445 | SMB | Windows File Sharing | **High** | ⚠️ |
| 993 | IMAPS | Secure Email | **Low** | ✅ |
| 995 | POP3S | Secure Email | **Low** | ✅ |
| 3389 | RDP | Remote Desktop | **Medium** | ⚠️ |
| 5900 | VNC | Remote Desktop | **High** | ⚠️ |

### Expected Results by Target

#### Localhost (127.0.0.1)
- **Common**: 22 (SSH), 53 (DNS), 631 (printing)
- **Development**: 3000, 5000, 8000 (web servers)
- **Database**: 3306 (MySQL), 5432 (PostgreSQL)

#### Windows Host
- **System**: 135 (RPC), 139 (NetBIOS), 445 (SMB)
- **Remote**: 3389 (RDP) if enabled
- **Web**: 80, 443 if IIS is running

#### Router
- **Management**: 80 (web interface), 22 (SSH)
- **Services**: 53 (DNS), 67 (DHCP)



## Safety Features

### Built-in Protections
1. **Private Network Detection** - Warns when scanning public IPs
2. **Rate Limiting** - Prevents overwhelming targets
3. **Input Validation** - Validates all user inputs
4. **Error Handling** - Graceful handling of network errors
5. **Confirmation Prompts** - Asks before scanning public networks

### Best Practices
- ✅ Always test on your own systems first
- ✅ Use virtual machines for practice
- ✅ Get written permission before scanning
- ✅ Document your testing procedures
- ✅ Respect rate limits and timeouts
- ❌ Never scan without authorization
- ❌ Don't scan production systems
- ❌ Avoid scanning during business hours


## License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🔗 Connect with Me


<div align="center">

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/m-raja-/)  [![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://rajam.vercel.app/)  [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/M-Raja)


</div>
<br>



<div align="center">

**Remember: With great power comes great responsibility. Use this tool ethically and legally!**



</div>





