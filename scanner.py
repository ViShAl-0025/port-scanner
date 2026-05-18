import socket

target = input("Enter IP or website: ")

print(f"\nScanning target: {target}\n")

ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")

    scanner.close()

print("\nScanning Completed.")