import socket
import select
import sys
import _thread
import re
import time

from src.middlewares.display import *
from src.middlewares.requestHandler import *
from src.controllers.AccountController import *
from src.controllers.UserController import *
from src.controllers.RoomController import *
from src.models.RoomRepository import *
from src.models.User import *
from src.models.Room import *

class Server:
    """
        main server class 
    """
    userController = UserController() #create instance of user controller
    roomController = RoomController() #create instance of room controller
    roomRepository = RoomRepository()

    def __init__(self, host, port):
        """
            constructor class for server
        """
        self.host = host
        self.port = port
        self.socket = ""
        self.clients = [] #list of connected clients
        self.users = []

    def createSocket(self):
        """
            create socket function
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except OSError as message:
            print('socket creation error: ' + str(message))

        
    def bindSocket(self):
        """
            start socket bindings
        """
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(100)

            print('server listening on port: ' + str(self.port))

        #auto reconnection every 3 seconds in case of errors
        except OSError as message:
            print('socket binding error: ' + str(message))
            print('retrying in 3 seconds...\n')
            time.sleep(3)
            self.bindSocket()


    def acceptConnection(self):
        """
            accept new connection request from new client and
            return it's connection object and address
        """
        conn, addr = self.socket.accept()
        print('\n' + str(addr) + ' connected')
        self.clients.append(conn) #add new connection to server's client list
        self.users.append('unknown')
        return conn, addr, len(self.users)

    
    def run(self, conn, addr, pos):
        """
            this function handles every client from any thread
            and return it's response
        """
        account = AccountController() #create an instance of current client account
        prefix = setPrefix(account) #set prefix

        #shows title in client
        self.sendMessage(conn, clearScreen())
        self.sendMessage(conn, displayColor('green') + 'welcome to chat app\n\n' + displayColor('white'))


        while True:
            """
                this loop handle client requests until
                it sends command to break and exit the app
            """
            try:
                request = self.waitMessage(conn, prefix) #recieves request from client
                if request:

                    if account.user != '':
                        message = displayColor('magenta') + account.user.username
                        message += displayColor('white') + '> ' + request
                        #print(message)
                        #self.broadcast(conn, message)

                    response = requestHandler(request, account, conn, self.clients) #handles and filters the request


                    if response == 'login':
                        """
                            condition to login an existing user
                        """
                        username = self.waitMessage(conn, '\nlogin: ')

                        password = self.waitMessage(conn, 'password: ' + displayColor('black'))
                        self.sendMessage(conn, displayColor('white'))

                        #if there is no user logged, create User instance
                        if account.user == '':
                            account.user = User(username, password)

                        response = account.login() #realizes login
                        self.users[pos] = account.user.username

                        #verify if login was succeful
                        if response != successMsg('logged in succefully'):
                            if response != errorMsg('you are already logged in'):
                                account.user = ''

                        print(account.user.username)
                        prefix = setPrefix(account)


                    
                    if response == 'logout':
                        """
                            condition to loggout a logged user
                        """
                        for i in range(len(self.users)):
                            if self.users[i] == account.user.username:
                                self.users[i] = 'unknown'
                        response = account.logout() #realizes logout


                        #verify is logout was succeful
                        if response == successMsg('logged out succefully'):
                            prefix = setPrefix(account)



                    if response == 'create user':
                        """
                            condition to create a new user
                        """

                        #verify if there is user logged in this client
                        if account.user != '':
                            response = errorMsg('you cannot create new account while logged')
                        else:
                            username = self.waitMessage(conn, '\nlogin: ')

                            password = self.waitMessage(conn, 'password: ' + displayColor('black'))
                            self.sendMessage(conn, displayColor('white'))

                            passwordConfirmation = self.waitMessage(conn, 'confirm password: ' + displayColor('black'))
                            self.sendMessage(conn, displayColor('white'))

                            if password != passwordConfirmation:
                                response = errorMsg('password does not match its confirmation')
                            else:
                                user = User(username, password)
                                response = self.userController.create(user) #create user

                    
                    if response == 'create room':
                        """
                            condition to create new room
                        """
                        if account.user == '':
                            response = errorMsg('you need to log in to create a room')
                        else:
                            name = self.waitMessage(conn, '\nroom name: ')
                            print(name)
                            print(account.user.username)
                            room = Room(name, account.user.username)
                            print(room)
                            # print(room)
                            print('aaaa')
                            response = self.roomController.create(room)


                    if response[:4] == 'join':
                        name = response[5:]

                        account.user.room = name
                        self.userController.update(account.user)
                        

                        self.sendMessage(conn, clearScreen())
                        message = displayColor('green') + 'you have joined ' + name + '\n\n' + displayColor('white')
                        self.sendMessage(conn, message)

                        while True:
                            try:
                                message = self.waitMessage(conn, '> ')
                                if message:
                                    self.broadcast(conn, name, message, account.user.username)
                        
                            except:
                                continue

                            


                    if response == 'exit':
                        """
                            condition to exit the app by logging out
                            and breaking the loop
                        """
                        self.sendMessage(conn, clearScreen())
                        self.sendMessage(conn, errorMsg('goodbye'))

                        #verify if user is not logged
                        if account.user != '':
                            username = account.user.username
                        response = account.logout()

                        if response == successMsg('logged out succefully'):
                            self.sendMessage(conn, username + ' ' + response +'\n')

                        self.closeConnection(conn, addr)
                        break

                    self.sendMessage(conn, response) #send the response back to the client


            except:
                continue





    def broadcast(self, conn, room, message):
        msg = displayColor('cyan') + message.center(100) + '\n' + displayColor('white')


        self.sendMessage(conn, msg)

        for i in range(len(self.clients)):
            if self.clients[i] != conn:
                user = self.userController.show(self.users[i])
                if user['room'] == room:
                    try:
                        self.sendMessage(client, message)
                    except:
                        self.clients[i].close()
                        self.remove(client)


    def remove(self, conn):
        for i in range(len(self.clients)):
            if self.clients == conn:
                self.clients.pop(i)
                self.users.pop(i)


    def sendMessage(self, conn, message):
        """
            function to handle and send messages to the client
        """
        message += '\n'
        conn.sendall(message.encode())


    def waitMessage(self, conn, prefix = ''):
        """
            function to handle and wait message from the client
        """
        conn.sendall(prefix.encode())
        message = conn.recv(1024).decode()   
        message = re.sub(r'\r\n', '', message)
        return message

    
    def closeConnection(self, conn, addr):
        """
            function to close client connection
        """

        for i in range(len(self.clients)):
            if self.clients == conn:
                self.clients.pop(i)
                self.users.pop(i)

        conn.close()
        print('\n' + str(addr) + ' disconnected')

    def closeServer(self):
        self.userController.logoutAll()

        #closes server's socket
        self.socket.close()





# host = '0.0.0.0'
# port = 8085

# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# socket.bind((host, port))

# socket.listen(100)

# clients = []

# def clientThread(conn, addr):
#     conn.send("welcome to chat room!".encode())

#     while True:
#         try:
#             message = conn.recv(2048).decode()
#             if message:
#                 message = f'<{addr[0]}> {message}'
#                 print(message)

#                 broadcast(message, conn)

#             else:
#                 remove(conn)

#         except:
#             continue


# def broadcast(message, conn):
#     for client in clients:
#         if client != conn:
#             try:
#                 client.send(message.encode())
#             except:
#                 client.close()
#                 remove(client)

# def remove(conn):
#     if conn in clients:
#         clients.remove(conn)

# while True:
#     conn, addr = socket.accept()
#     clients.append(conn)
#     print(f'{addr[0]} connected')

#     _thread.start_new_thread(clientThread, (conn, addr))

# conn.close()
# socket.close()
