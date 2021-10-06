import socket
import sys
import time

def change_channel():
# Create a UDP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_address = ('10.18.20.103', 23456)
	message = '5500004000080004000400d82a619eaa'.decode('hex') #number 1
	message = '5500004000080004000400d82a629daa'.decode('hex') #number 2
	message = '5500004000080004000400d82a639caa'.decode('hex') #number 3
	message = '5500004000080004000400d82a649baa'.decode('hex') #number 4
	message = '5500004000080004000400d82a659aaa'.decode('hex') #number 5
	message = '5500004000080004000400d82a6699aa'.decode('hex') #number 6
	message = '5500004000080004000400d82a6798aa'.decode('hex') #number 7
	message = '5500004000080004000400d82a6897aa'.decode('hex') #number 8
	message = '5500004000080004000400d82a6996aa'.decode('hex') #number 9
	message = '5500004000080004000400d82a609faa'.decode('hex') #number 0
	message1 = '5500004000080004000400d82a6798aa'.decode('hex') #number 7
	message2 = '5500004000080004000400d82a6798aa'.decode('hex') #number 7

	message1 = '5500004000080004000400d82a6897aa'.decode('hex') #number 8
	message2 = '5500004000080004000400d82a639caa'.decode('hex') #number 3
	
	message1 = '5500004000080004000400d82a6996aa'.decode('hex') #number 9
	message2 = '5500004000080004000400d82a6699aa'.decode('hex') #number 6

	try:

		# Press 1st button
		print >>sys.stderr, 'sending "%s"' % message1
		sent = sock.sendto(message1, server_address)

		# Press 2nd button
		print >>sys.stderr, 'sending "%s"' % message2
		sent = sock.sendto(message2, server_address)

	finally:
		print >>sys.stderr, 'closing socket'
		sock.close()

start_time = time.time()

while time.time() - start_time < 60:
#	print(x)
	change_channel()
	print("--- %s seconds ---" % (time.time() - start_time))
	time.sleep(5)
