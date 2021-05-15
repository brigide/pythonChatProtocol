from src.models.User import User
from src.models.UserRepository import UserRepository
from src.middlewares.display import *
import json 


class AccountController:
    
    def __init__(self):
        self.userRepository = UserRepository()
        self.user = ''


    def login(self):
        user = self.userRepository.findByUsername(self.user.username)

        if user == None:
            return errorMsg('user not found')

        if user['password'] != self.user.password:
            return errorMsg('incorrect password')

        if self.user.isLogged == True:
            return errorMsg(self.user.username + ' already logged in')
        
        self.user.isLogged = True

        self.userRepository.update(self.user)

        return successMsg('logged in succefully')


    def logout(self):
        if self.user == '':
            return errorMsg('no user logged')

        user = self.userRepository.findByUsername(self.user.username)

        if user == None:
            return errorMsg('user not found')


        self.user.isLogged = False
        self.user.room = ""

        self.userRepository.update(self.user)

        self.user = ''

        return successMsg('logged out succefully')


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

        
