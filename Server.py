from socket import *
import re

from src.middlewares.display import *
from src.middlewares.requestHandler import *


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = ""
        self.conn = ""
        self.addr = ""


    def createSocket(self):
        try:
            self.socket = socket(AF_INET, SOCK_STREAM)

        except error as message:
            print('socket creation error: ' + str(message))

        
    def bindSocket(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)

            print('server listening on port: ' + str(self.port))

        except error as message:
            print('socket binding error: ' + str(message))
            print('retrying...')
            self.bindSocket()


    def acceptConnection(self):
        self.conn, self.addr = self.socket.accept()

    
    def init(self):
        self.sendMessage(clearScreen())
        self.sendMessage(displayColor('green') + 'welcome to chat app\n\n' + displayColor('white'))

        while True:
            request = self.waitMessage()

            response = requestHandler(request)

            if response == 'exit':
                self.sendMessage(clearScreen())
                self.sendMessage(displayColor('red') + 'goodbye\n' + displayColor('white'))
                break

            self.sendMessage(response)




    def sendMessage(self, message):
        message += '\n'
        self.conn.sendall(message.encode())


    def waitMessage(self):
        self.conn.sendall('chat> '.encode())
        message = self.conn.recv(1024).decode()   
        message = re.sub(r'\r\n', '', message)
        return message

    
    def closeConnection(self):
        self.conn.close()

    def closeSocket(self):
        self.socket.close()