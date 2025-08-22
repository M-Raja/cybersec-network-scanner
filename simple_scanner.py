#!/usr/bin/env python3
"""
Simple Network Scanner - Beginner Version
Your first step into ethical hacking!
Author: [Your Name]
"""

import socket
import sys
import time
import re
import threading

def is_private_network(ip):
    """Check if IP is in private network ranges"""
    parts = ip.split('.')
    first_octet = int(parts[0])
    
    # Private network ranges
    if first_octet == 10:
        return True
    elif first_octet == 172 and 16 <= int(parts[1]) <= 31:
        return True
    elif first_octet == 192 and int(parts[1]) == 168:
        return True
    elif ip == "127.0.0.1":
        return True
    
    return False

def validate_ip(ip):
    """Validate IP address format"""
    if not ip or not isinstance(ip, str):
        return False
    
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    
    parts = ip.split('.')
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True

def validate_port(port):
    """Validate port number"""
    try:
        port_num = int(port)
        return 1 <= port_num <= 65535
    except ValueError:
        return False

def check_host_alive(ip):
    """Check if a host is alive by trying to connect to port 80"""
    try:
        # Create a socket (think of it as a phone call)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Increased timeout for better reliability
        
        # Try to connect to port 80 (web server)
        result = sock.connect_ex((ip, 80))
        sock.close()
        
        if result == 0:
            return True
        else:
            return False
    except (socket.error, OSError, ValueError) as e:
        print(f"Error checking host: {e}")
        return False

def scan_single_port(ip, port):
    """Scan one port on one IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Increased timeout for better reliability
        
        # Try to connect
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            print(f"✓ Port {port} is OPEN on {ip}")
            return True
        else:
            return False
    except socket.timeout:
        # Port is filtered or host is unreachable
        return False
    except socket.gaierror as e:
        print(f"Error resolving hostname for port {port}: {e}")
        return False
    except (socket.error, OSError, ValueError) as e:
        print(f"Error scanning port {port}: {e}")
        return False

def scan_common_ports(ip):
    """Scan the most common ports"""
    print(f"\n🔍 Scanning common ports on {ip}...")
    
    # These are the most common ports you'll find open
    common_ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 993, 995, 3389, 5900]
    open_ports = []
    
    for port in common_ports:
        if scan_single_port(ip, port):
            open_ports.append(port)
        # Small delay to be respectful
        time.sleep(0.1)
    
    return open_ports

def scan_port_range(ip, start_port, end_port):
    """Scan a range of ports"""
    print(f"\n🔍 Scanning ports {start_port}-{end_port} on {ip}...")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if scan_single_port(ip, port):
            open_ports.append(port)
        
        # Show progress every 50 ports
        if port % 50 == 0:
            print(f"📊 Progress: Scanned up to port {port}")
        
        # Small delay to be respectful
        time.sleep(0.05)
    
    return open_ports

def banner_grab(ip, port):
    """Try to grab service banner/version info"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))
        
        # Try to get banner based on port type
        if port == 80 or port == 8080:
            # HTTP request
            sock.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode('utf-8') + b"\r\n\r\n")
        elif port == 22:
            # SSH - just try to read initial banner
            pass
        elif port == 21:
            # FTP - send simple command
            sock.send(b"HELP\r\n")
        elif port == 25:
            # SMTP - send simple command
            sock.send(b"HELP\r\n")
        else:
            # Generic banner grab - just send newline
            sock.send(b"\r\n")
        
        banner = sock.recv(1024).decode('utf-8', errors='ignore')
        sock.close()
        
        # Clean up the banner
        banner = banner.strip()
        if banner:
            return banner[:100]  # First 100 characters
        return None
    except (socket.error, OSError, ValueError, UnicodeError) as e:
        # Silently handle banner grab errors - they're not critical
        return None

def main():
    """Main function - this runs when you execute the script"""
    print("🚀 Simple Network Scanner Starting...")
    print("=" * 40)
    
    # Get target IP from user
    while True:
        target_ip = input("Enter target IP address (try 127.0.0.1 first): ").strip()
        if validate_ip(target_ip):
            # Safety check for private networks
            if is_private_network(target_ip):
                print("✅ Scanning private network/localhost - this is safe for testing!")
            else:
                print("⚠️  Warning: You're scanning a public IP address.")
                confirm = input("Are you sure you want to continue? (y/N): ").strip().lower()
                if confirm not in ['y', 'yes']:
                    print("Scan cancelled for safety.")
                    return
            break
        else:
            print("❌ Invalid IP address format. Please enter a valid IP (e.g., 127.0.0.1)")
    
    # Step 1: Check if host is alive
    print(f"\n📡 Checking if {target_ip} is alive...")
    if check_host_alive(target_ip):
        print(f"✅ {target_ip} is alive!")
    else:
        print(f"❌ {target_ip} seems down or port 80 is closed")
        print("Don't worry, let's scan anyway!")
    
    # Step 2: Ask user what type of scan
    print("\nChoose scan type:")
    print("1. Quick scan (common ports)")
    print("2. Range scan (specify ports)")
    print("3. Full scan (1-1000)")
    
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
    
    if choice == "1":
        open_ports = scan_common_ports(target_ip)
    elif choice == "2":
        while True:
            start_input = input("Start port (1-65535): ").strip()
            if validate_port(start_input):
                start = int(start_input)
                break
            else:
                print("❌ Invalid start port. Please enter a number between 1-65535.")
        
        while True:
            end_input = input("End port (1-65535): ").strip()
            if validate_port(end_input):
                end = int(end_input)
                if end >= start:
                    break
                else:
                    print("❌ End port must be greater than or equal to start port.")
            else:
                print("❌ Invalid end port. Please enter a number between 1-65535.")
        
        open_ports = scan_port_range(target_ip, start, end)
    elif choice == "3":
        print("⚠️  This will take a while...")
        open_ports = scan_port_range(target_ip, 1, 1000)
    
    # Step 3: Show results
    print(f"\n📊 SCAN RESULTS for {target_ip}")
    print("=" * 40)
    
    if open_ports:
        print(f"Found {len(open_ports)} open ports:")
        for port in open_ports:
            # Tell user what each port typically is used for
            port_info = {
                21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
                80: "HTTP", 135: "RPC", 139: "NetBIOS", 443: "HTTPS", 
                445: "SMB", 993: "IMAPS", 995: "POP3S", 3389: "RDP", 5900: "VNC"
            }
            service = port_info.get(port, "Unknown")
            
            # Try to grab banner
            banner = banner_grab(target_ip, port)
            banner_info = f" - {banner[:50]}..." if banner else ""
            
            print(f"  Port {port}: {service}{banner_info}")
    else:
        print("No open ports found")
    
    print(f"\n✨ Scan complete!")

# This runs when you execute the script
if __name__ == "__main__":
    main()