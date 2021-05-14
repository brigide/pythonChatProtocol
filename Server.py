from socket import *
import re
import time

from src.middlewares.display import *
from src.middlewares.requestHandler import *
from src.controllers.AccountController import *
from protocols import protocols


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = ""
        self.conn = ""
        self.addr = ""
        self.account = ""


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

        except OSError as message:
            print('socket binding error: ' + str(message))
            print('retrying in 3 seconds...\n')
            time.sleep(3)
            self.bindSocket()


    def acceptConnection(self):
        self.conn, self.addr = self.socket.accept()
        print('\n' + str(self.addr) + ' connected')

    
    def init(self):
        self.sendMessage(clearScreen())
        self.sendMessage(displayColor('green') + 'welcome to chat app\n\n' + displayColor('white'))

        while True:
            request = self.waitMessage()

            response = requestHandler(request)

            if response == 'login':
                username = self.waitMessage('login: ')

                password = self.waitMessage('password: ' + displayColor('black'))
                self.sendMessage(displayColor('white'))

                self.account = AccountController(username, password)

                response = self.account.login()


            if response == 'exit':
                self.sendMessage(clearScreen())
                self.sendMessage(displayColor('red') + 'goodbye\n' + displayColor('white'))
                break

            self.sendMessage(response)




    def sendMessage(self, message):
        message += '\n'
        #message = message.center(100)
        self.conn.sendall(message.encode())


    def waitMessage(self, prefix = 'chat> '):
        self.conn.sendall(prefix.encode())
        message = self.conn.recv(1024).decode()   
        message = re.sub(r'\r\n', '', message)
        return message

    
    def closeConnection(self):
        print('\n' + str(self.addr) + ' disconnected')
        self.conn.close()

    def closeSocket(self):
        self.socket.close()