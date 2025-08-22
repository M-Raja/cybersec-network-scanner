# Network Vulnerability Scanner

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg?style=for-the-badge)

**A comprehensive network port scanner and vulnerability assessment tool built in Python for educational penetration testing.**

 [Documentation](docs/setup_and_usage.md) • [Safety](#safety-features) • [Learning](#educational-resources)

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


## Installation

### Method 1: Quick Installation

1. **Clone or Download the Project**
   ```bash
   # Option A: Clone from repository
   git clone https://github.com/M-Raja/cybersec-network-scanner
   cd network-vulnerability-scanner
   
   # Option B: Download and extract ZIP file
   # Extract to your desired directory
   ```

2. **Install Dependencies**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   # Test the scanner
   python3 simple_scanner.py --help
   ```

### Method 2: Virtual Environment Installation (Recommended)

1. **Create Virtual Environment in linux**
   ```bash
   # Create virtual environment
   python3 -m venv scanner_env
   
   # Activate virtual environment
   # On Windows:
   scanner_env\Scripts\activate
   
   # On Linux/macOS:
   source scanner_env/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   # Install packages in virtual environment
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   # Test the scanner
   python3 simple_scanner.py --help
   ```

### Method 3: System-Wide Installation

1. **Install System Dependencies (Linux)**
   ```bash
   # Update package list
   sudo apt update
   
   # Install Python and pip
   sudo apt install python3 python3-pip python3-venv
   
   # Install nmap (optional)
   sudo apt install nmap
   ```

2. **Install Python Dependencies**
   ```bash
   # Install required packages
   pip3 install -r requirements.txt
   ```

---


### Environment Setup

1. **Network Configuration**
   - Ensure your network allows outbound connections
   - Configure firewall if necessary
   - Verify DNS resolution

2. **Python Environment**
   - Verify Python version: `python --version`
   - Check pip installation: `pip --version`
   - Ensure virtual environment is activated (if using)

3. **Scanner Configuration**
   - No additional configuration files required
   - Settings are handled through command-line arguments
   - Default settings are optimized for educational use

### Security Considerations

1. **Authorization**
   - Only scan systems you own or have explicit permission to test
   - Obtain written authorization before scanning any network
   - Document your testing scope and procedures

2. **Network Impact**
   - The scanner includes rate limiting to minimize network impact
   - Default timeouts prevent overwhelming target systems
   - Use appropriate scan types for your environment



## Basic Usage

### Interactive Mode

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



## Understanding Results

### Port States
- **OPEN** - Service is running and accepting connections
- **CLOSED** - Port is reachable but no service listening
- **FILTERED** - Firewall blocking the port
- **UNREACHABLE** - Host is down or network issue

### Service Information
- **Banner Grabbing** - Attempts to identify service versions
- **Protocol Detection** - Identifies the protocol in use
- **Service Mapping** - Maps ports to common services

### Risk Assessment
- **High Risk** - Unencrypted services, default credentials
- **Medium Risk** - Services with known vulnerabilities
- **Low Risk** - Properly configured secure services



## Troubleshooting

### Common Issues

#### "Connection Refused"
- Target is not running the service
- Firewall is blocking connections
- Wrong IP address

#### "Timeout"
- Network is slow
- Target is filtering connections
- Service is not responding

#### "Permission Denied"
- Need administrative privileges
- Firewall blocking outbound connections
- Network restrictions

### Debug Mode
```bash
# Enable verbose output
python3 simple_scanner.py --verbose --debug

# Check network connectivity
ping -c 4 [target_ip]

# Test specific port manually
telnet [target_ip] [port]
```

## Practice Scenarios

### Beginner Exercises
1. **Local Network Mapping**
   - Scan your home network
   - Document all devices found
   - Identify potential security issues

2. **Service Enumeration**
   - Find web servers on your network
   - Identify database servers
   - Map file sharing services

3. **Vulnerability Research**
   - Research common vulnerabilities for found services
   - Practice on intentionally vulnerable systems
   - Learn about patch management

### Advanced Exercises
1. **Custom Scripts** - Extend the scanner with new features
2. **Automation** - Create automated scanning workflows
3. **Reporting** - Generate professional security reports
4. **Integration** - Combine with other security tools



## License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🔗 Connect with Me

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/m-raja-/)
- [![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://rajam.vercel.app/)
- [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/M-Raja)

<br>



<div align="center">

**Remember: With great power comes great responsibility. Use this tool ethically and legally!**

[Back to Top](#network-vulnerability-scanner)

</div>


