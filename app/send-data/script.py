import socket

server = "127.0.0.1"
port = 514

with open("../../logs/firewall.log", "r") as f:
    for line in f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(line.strip().encode("ascii"), (server, port))
        sock.close()
