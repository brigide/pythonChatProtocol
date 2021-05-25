class Room:
    
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.users = []
        self.conns = []
        

    def getRoom(self):
        room = {
            "name": self.name,
            "admin": self.admin,
            "users": self.users,
            "conns": self.conns
        }
        return room

    @property
    def name(self):
        print(self.name)
        print(self._name)
        return self._name

    @name.setter
    def name(self, name):
        print(self.name)
        print(self._name)
        self._name = name

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, admin):
        self._admin = admin

    @property
    def users(self):
        return self.isLogged

    @users.setter
    def users(self, user):
        self.users.append(user)

    @property
    def conns(self):
        return self.conns
