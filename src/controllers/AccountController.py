from src.models.User import User
from src.models.UserRepository import UserRepository
import json 


class AccountController:
    userRepository = UserRepository()
    
    def __init__(self, username, password):
        self.user = User(username, password)


    def status(self):
        return self.user.isLogged

    def login(self):
        user = self.userRepository.findByUsername(self.user.username)

        if user == None:
            return 'user not found'

        if user['password'] != self.user.password:
            return 'incorrect password'
        
        self.user.isLogged = True

        self.userRepository.update(self.user)

        return 'logged in succefully'


    def logout(self):
        user = self.userRepository.findByUsername(self.user.username)

        if user == None:
            return 'user not found'

        self.user.isLogged = False
        self.user.room = ""

        self.userRepository.update(self.user)

        return 'logged out succefully'

        
