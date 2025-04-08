import socket
import threading

# Optional: common port descriptions
port_descriptions = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3",
    143: "IMAP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"
}

# Scan logic for a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            result = s.connect_ex((ip, port))
            if result == 0:
                desc = port_descriptions.get(port, "Unknown service")
                print(f"✅ Port {port} is OPEN ({desc})")
    except Exception as e:
        pass  # Silently ignore failed ports

# Main function
def main():
    print("🚀 Simple Network Port Scanner")
    print("⚠️ Only scan authorized systems!\n")

    target = input("Enter target IP address: ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Scan complete.")

if __name__ == "__main__":
    main()
