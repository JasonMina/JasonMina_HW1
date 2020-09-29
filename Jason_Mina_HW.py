import struct
import socket
n=bytes()
server1 = "time-a-b.nist.gov"
server2= "utcnist.colorado.edu"
port = 37
receive_buffer_size = 4096
# Create socket

mysocket1 = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
mysocket2 = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# or simply socket.socket( ) – which defaults to above

# Connect to server
mysocket1.connect( ( server1, port ) )
mysocket2.connect( ( server2, port ) )


# Send request
mysocket1.send(n)
mysocket2.send(n)

# Receive response
response_time1 = mysocket1.recv( receive_buffer_size )
response_time2 = mysocket2.recv( receive_buffer_size )
# Close socket

time1=int.from_bytes(response_time1, byteorder='big')
time2=int.from_bytes(response_time2, byteorder='big')

def timeprint (time, socket_number):
    if socket_number==1:
        print ("Server 1 of address", server1, "and IP address", socket.gethostbyname(server1))
    if socket_number==2:
         print ("Server 2 of address", server2, "and IP address", socket.gethostbyname(server2))
    print (" Has a liftime of", time, "seconds since 00:00 AM, January 1990" )
    years = time // (365 * 24 * 3600)
    
    print ("Year number since 1900: ", years)
    print ("which is year", 1900 + years)

timeprint(time1, 1)
timeprint(time2, 2)
time_difference= abs(time1 - time2)
print ("The time difference between the two servers is", time_difference, "seconds")
mysocket1.close
mysocket2.close
# Print response










































