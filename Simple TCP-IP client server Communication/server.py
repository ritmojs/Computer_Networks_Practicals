import socket			                

s = socket.socket()		                
host = socket.gethostname()	            
port = 123
s.bind((host,port))		                

print("Waiting for connection...")
s.listen(5)
while True:
	conn,addr = s.accept()
	print('Got Connection from', addr)
	conn.send(b'Connection accepted')
	conn.close()		                
