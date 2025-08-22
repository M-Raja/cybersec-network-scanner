# Network Vulnerability Scanner

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg?style=for-the-badge)

**A comprehensive network port scanner and vulnerability assessment tool built in Python for educational penetration testing.**

[Quick Start](#quick-start) • [Documentation](docs/setup_and_usage.md) • [Safety](#safety-features) • [Learning](#educational-resources)

</div>

---

## ⚠️ **CRITICAL DISCLAIMER**

<div align="center">

**This tool is for EDUCATIONAL PURPOSES ONLY!**

</div>

- Only scan networks and systems you **OWN** or have **EXPLICIT PERMISSION** to test
- Unauthorized scanning is **ILLEGAL** in most jurisdictions
- Use responsibly and ethically
- You are responsible for ensuring proper authorization

---

## Project Overview

This scanner helps you learn:
- **Network reconnaissance** techniques
- **Port scanning** methodologies  
- **Service identification** and banner grabbing
- **Ethical hacking** fundamentals
- **Vulnerability assessment** basics

---

## Prerequisites

### System Requirements
- Kali Linux VM (recommended) or any Linux distribution
- Python 3.6+
- Network connectivity
- Administrative privileges (for some features)

### Required Packages
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
sudo apt install python3-pip python3-venv nmap -y

# Install Python requirements
pip install -r requirements.txt
```

---

## Quick Start

> **📖 For detailed setup instructions, see [Setup and Usage Guide](docs/setup_and_usage.md)**

### Step 1: Clone & Setup
```bash
# Create project directory
mkdir ~/network_vuln_scanner
cd ~/network_vuln_scanner

# Create virtual environment
python3 -m venv scanner_env
source scanner_env/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

### Step 2: Download Scanner
```bash
# Download the scanner
wget https://raw.githubusercontent.com/your-repo/simple_scanner.py
# OR copy the simple_scanner.py file to your project directory

# Make executable
chmod +x simple_scanner.py
```

### Step 3: Run Your First Scan
```bash
# Test the scanner
python3 simple_scanner.py

# Enter: 127.0.0.1 (localhost - always safe!)
# Choose: 1 (Quick scan)
```

---

## Usage Guide

### Interactive Mode
The scanner will prompt you for:
1. **Target IP Address** - Enter the IP you want to scan
2. **Scan Type** - Choose from:
   - Quick scan (common ports)
   - Range scan (custom ports)
   - Full scan (1-1000)

### Command Line Options
```bash
# Scan specific IP
python3 simple_scanner.py --target 127.0.0.1

# Quick scan only
python3 simple_scanner.py --quick

# Verbose output
python3 simple_scanner.py --verbose
```

---

## Testing & Practice

### Safe Testing Targets (In Order of Safety)

#### 1. Localhost (Always Safe)
```bash
# Target: 127.0.0.1
# Expected: Local services, development servers
python3 simple_scanner.py
# Enter: 127.0.0.1
```

#### 2. Your Own VM
```bash
# Find your VM's IP
ip addr show

# Look for: 192.168.x.x or 10.0.x.x
# Example: 10.0.2.15 (NAT network)
```

#### 3. Your Windows Host
```bash
# On Windows CMD:
ipconfig
# Note the IPv4 Address

# From Kali, scan that IP
```

#### 4. Your Router (Be Careful!)
```bash
# Usually: 192.168.1.1 or 10.0.0.1
# Only scan your own router!
```

### Finding IP Addresses

#### In Kali Linux:
```bash
# Show all network interfaces
ip addr show

# Show routing table
ip route show

# Quick IP check
hostname -I
```

#### In Windows:
```bash
# Open CMD and type:
ipconfig

# Look for "IPv4 Address" under your active adapter
```

---

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

---

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

---

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

---

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

---

## Educational Resources

### Learning Path
1. **Network Fundamentals** - Understand TCP/IP, ports, protocols
2. **Reconnaissance** - Learn passive and active information gathering
3. **Vulnerability Assessment** - Identify security weaknesses
4. **Penetration Testing** - Ethical hacking methodologies
5. **Security Hardening** - Learn to secure systems

### Recommended Reading
- "The Web Application Hacker's Handbook"
- "Network Security Essentials" by William Stallings
- "Hacking: The Art of Exploitation" by Jon Erickson
- NIST Cybersecurity Framework
- OWASP Top 10

### Online Resources
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [VulnHub](https://www.vulnhub.com/)

---

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

---

## Legal & Ethical Considerations

### Legal Requirements
- **Authorization** - Always get written permission
- **Scope** - Define clear testing boundaries
- **Documentation** - Keep detailed records
- **Compliance** - Follow relevant regulations

### Ethical Guidelines
- **Do No Harm** - Avoid disrupting services
- **Respect Privacy** - Don't access unauthorized data
- **Professional Conduct** - Maintain confidentiality
- **Continuous Learning** - Stay updated on best practices

---

## Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Add comprehensive comments
- Include error handling
- Write unit tests
- Update documentation

---

## Support & Community

### Getting Help
- Check the troubleshooting section
- Search existing issues
- Create a detailed bug report
- Join the community discussions

### Community Guidelines
- Be respectful and professional
- Help others learn
- Share knowledge responsibly
- Report security issues privately

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by educational security tools
- Built with open-source libraries
- Community contributions welcome
- Special thanks to the security research community

---

## 🔗 Connect with Me

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/m-raja-/)
- [![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://rajam.vercel.app/)
- [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/M-Raja)

<br>

---

<div align="center">

**Remember: With great power comes great responsibility. Use this tool ethically and legally!**

[Back to Top](#network-vulnerability-scanner)

</div>
