import socket
import pickle
from mainclass import MainClass

HOST = 'localhost'
PORT = 50007
# Creating a sokcet connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Create an instance of ProcessData() to send to server.
variable =  MainClass("89")
# Pickle the object and send it to the server
data_string = pickle.dumps(variable)
s.send(data_string)

s.close()

print 'Data has been sent to the Server'