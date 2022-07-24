import socket

SERVER_IP = '192.168.56.1'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((SERVER_IP,SERVER_PORT))
	s.listen(1)
	print('Server Listening...')
	conn, addr = s.accept()
	print(f'Connection Established from {addr}')
	with conn:
		while True:
			conn.send(b'Hello world')
			break