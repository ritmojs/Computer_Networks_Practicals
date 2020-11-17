
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

udp_host = socket.gethostname()		
udp_port = 123			        

msg = "Hello Python!"
print("UDP target IP:", udp_host)
print("UDP target Port:", udp_port)

sock.sendto(bytes(msg, "utf-8"),(udp_host,udp_port))		
sock.close()
