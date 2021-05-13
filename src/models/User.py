class User:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLogged = False
        self.room = ""

    def getUser(self):
        user = {
            "username": self.username,
            "password": self.password,
            "isLogged": self.isLogged,
            "room": self.room
        }
        return user

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.password

    @property
    def isLogged(self):
        return self.isLogged

    @isLogged.setter
    def isLogged(self, isLogged):
        self.isLogged = isLogged

    @property
    def room(self):
        return self.room

    @room.setter
    def room(self, room):
        self.room = room

