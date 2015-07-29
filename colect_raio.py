#!/usr/local/bin/python2.7
import socket
import struct

x = 0

while x != 1:

	HOST, PORT = "lx.datamart.earthnetworks.com", 80
	data = '{"p":"784B45BB-2BA6-45B0-8250-91BD70CBBD18","v":3,"f":2,"t":3}'

	try:
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    sock.connect((HOST, PORT))
	    sock.sendall(data + "\n")
	    received = sock.recv(1024)
	    raio = list(struct.unpack(''+str(len(received))+'B', received))
	    print(raio)
	    file_raio = open('convert', 'a')
	    file_raio.write(str(raio)+'\n')
	    file_raio.close()
	    print(hex(raio[1]).replace('0x',''))
	finally:
	    sock.close()
