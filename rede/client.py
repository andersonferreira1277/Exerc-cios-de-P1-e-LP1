from socket import *
serverName = "localhost"
serverPort = 1277
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


while True:
	sentence = input("Input lowercase sentence:")
	clientSocket.send(sentence.encode(encoding='utf-8'))
	print ("Preparando pra enviar")
	modifiedSentence = clientSocket.recv(1024)
	print ("enviou...")
	print ("From Server: ", modifiedSentence)

clientSocket.close()