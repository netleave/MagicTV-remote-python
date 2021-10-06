import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.18.20.103', 23456)
#message = 'This is the message.  It will be repeated.'
#message = '5500004040080004000400d82a708faa'.decode('hex')
#message = '55000040400e00040289d5334f0000000002006000aa'.decode('hex')
#message = '5500004040140000021ed949450000000008000064600000000308aa'.decode('hex')
#message = '550000404014000002610e1f230000000008000064600000000308aa'.decode('hex')
#message = '550000404014000002e56036610000000008000064600000000308aa'.decode('hex')
#message = '55000040802900020025000000e0014001342e322e31000000fe42fa532055eaf052a66d99207195f1636869dfcfcd4eaa'.decode('hex')
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
message = '5500004000080004000400d82a6996aa'.decode('hex') #number 9

																
try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
#    print >>sys.stderr, 'waiting to receive'
#    data, server = sock.recvfrom(4096)
##    print >>sys.stderr, 'received "%s"' % data
#    print >>sys.stderr, 'received "%s"' % data.encode('hex')
#    print >>sys.stderr, 'sub-rece "%s"' % data[11:-5].encode('hex')

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#message = 'This is the message.  It will be repeated.'
#message = '5500004040080004000400d82a708faa'.decode('hex')
#message = '55000040400e00040289d5334f0000000002006000aa'.decode('hex')
#message = '5500004040140000021ed949450000000008000064600000000308aa'.decode('hex')
#message = '550000404014000002610e1f230000000008000064600000000308aa'.decode('hex')
#message = '550000404014000002e56036610000000008000064600000000308aa'.decode('hex')
#message = '55000040802900020025000000e0014001342e322e31000000fe42fa532055eaf052a66d99207195f1636869dfcfcd4eaa'.decode('hex')
#message = ('550000404014000002'+data[11:-5].encode('hex')+'000000000800000A600000000308aa').decode('hex')
message = '5500004000080004000400d82a6996aa'.decode('hex') #number 9

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
#    print >>sys.stderr, 'waiting to receive'
#    data, server = sock.recvfrom(4096)
##    print >>sys.stderr, 'received "%s"' % data
#    print >>sys.stderr, 'received "%s"' % data.encode('hex')
##    print >>sys.stderr, 'sub-rece "%s"' % data[11:-5].encode('hex')

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

