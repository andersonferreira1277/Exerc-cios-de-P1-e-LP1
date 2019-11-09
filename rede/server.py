from socket import *
import _thread
import random

serverPort = 1277
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)


def task(connection, client):
	print (connection)
	print (client)
	id = random.randint(0, 10000)
	while True:
		received = connection.recv(1024)
		print ("servidor recebeu mensagem ", received, " do cliente ", id)
		capitalizedSentence = received.upper()
		print(received)
		connection.send(capitalizedSentence)

	connection.close()

print ("The server is ready to receive")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))