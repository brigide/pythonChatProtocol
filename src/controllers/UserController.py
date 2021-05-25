from src.models.User import User
from src.models.UserRepository import UserRepository
from src.middlewares.display import *
import json 


class UserController:
    userRepository = UserRepository()

    def __init__(self):
        pass


    def index(self, status = None):
        if status == 'online':
            return self.userRepository.fetchLogged()

        return self.userRepository.fetchAll()

    
    def show(self, username):
        user = self.userRepository.findByUsername(username)

        if user == None:
            return 'user not found'
        
        return user


    def create(self, user):
        if self.userRepository.findByUsername(user.username) != None:
            return errorMsg('username already in use')

        self.userRepository.save(user)

        return successMsg('user created succefully')

    
    def update(self, user):
        if self.userRepository.findByUsername(user.username) == None:
            return errorMsg('user not found')
        
        self.userRepository.update(user)

        return successMsg('user updated succefully')


    def delete(self, user):
        if self.userRepository.findByUsername(user.username) == None:
            return errorMsg('user not found')

        self.userRepository.delete(user)

        return successMsg('user removed succefully')


    def logoutAll(self):
        """
            method to set all users offline
            prevent any bug and crash some user's login
        """
        users = self.userRepository.fetchLogged()
        if users != 'no online users':
            for user in users:
                user['isLogged'] == False
                usr = User(user['username'], user['password'])
                self.userRepository.update(usr)