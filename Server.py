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
        self.account = AccountController()
        self.prefix = displayColor('cyan') + 'chat@' 
        self.prefix += displayColor('cyan') + 'unknown' + displayColor('white')


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
                username = self.waitMessage('\nlogin: ')

                password = self.waitMessage('password: ' + displayColor('black'))
                self.sendMessage(displayColor('white'))

                if self.account.user == '':
                    self.account.user = User(username, password)

                response = self.account.login()

                if response == successMsg('logged in succefully'):
                    self.prefix = displayColor('cyan') + 'chat@' 
                    self.prefix += displayColor('yellow') + self.account.user.username
                    self.prefix += displayColor('white')

            
            if response == 'logout':
                response = self.account.logout()

                if response == successMsg('logged out succefully'):
                    self.prefix = displayColor('cyan') + 'chat@' 
                    self.prefix += displayColor('cyan') + 'unknown' + displayColor('white')

            if response == 'exit':
                self.sendMessage(clearScreen())
                self.sendMessage(displayColor('red') + 'goodbye' + displayColor('white'))
                if self.account.user != '':
                    username = self.account.user.username
                response = self.account.logout()

                if response == successMsg('logged out succefully'):
                    self.sendMessage(username + ' ' + response +'\n')
                break

            self.sendMessage(response)




    def sendMessage(self, message):
        message += '\n'
        #message = message.center(100)
        self.conn.sendall(message.encode())


    def waitMessage(self, prefix = ''):
        if prefix == '':
            prefix = f'{self.prefix}> '
        self.conn.sendall(prefix.encode())
        message = self.conn.recv(1024).decode()   
        message = re.sub(r'\r\n', '', message)
        return message

    
    def closeConnection(self):
        print('\n' + str(self.addr) + ' disconnected')
        self.conn.close()

    def closeSocket(self):
        self.socket.close()