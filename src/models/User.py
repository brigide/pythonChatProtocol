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
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def isLogged(self):
        return self._isLogged

    @isLogged.setter
    def isLogged(self, isLogged):
        self._isLogged = isLogged

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

