from src.models.User import User
from src.models.UserRepository import UserRepository
from src.middlewares.display import *
import json 


class AccountController:
    """
        controller class to menage single client account
    """
    
    def __init__(self):
        """
            constructor method
        """
        self.userRepository = UserRepository()
        self.user = ''


    def login(self):
        """
            login function
        """
        #search for an user matching given username
        user = self.userRepository.findByUsername(self.user.username)

        #verify if current client is logged in 
        if self.user.isLogged == True:
            return errorMsg('you are already logged in')

        #verify if given username matches an existing user
        if user == None:
            return errorMsg('user not found, use "create account" to register a new account')

        #verify if given pass matches user pass
        if user['password'] != self.user.password:
            return errorMsg('incorrect password')

        #verify if guven user is logged in any other client
        if user['isLogged'] == True:
            return errorMsg(user['username'] + ' already logged in')
        
        self.user.isLogged = True #set user as logged

        self.userRepository.update(self.user) #update database to set user logged

        return successMsg('logged in succefully')


    def logout(self):
        """
            logout function
        """

        #verify if there is user logged in current client
        if self.user == '':
            return errorMsg('no user logged')

        #search and verify if user exist
        user = self.userRepository.findByUsername(self.user.username)

        if user == None:
            return errorMsg('user not found')


        #logout and update status in database
        self.user.isLogged = False
        self.user.room = ""

        self.userRepository.update(self.user)

        self.user = ''

        return successMsg('logged out succefully')


    #getter and setter for user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

        
