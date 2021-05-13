from socket import *
#from middlewares.auth import auth

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)

print("Server listening on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    
    isLogged = False

    request = connectionSocket.recv(1024).decode()
    response = "Connected: " + str(request)

    connectionSocket.sendall(response.encode())

    connectionSocket.close()

serverSocket.close()