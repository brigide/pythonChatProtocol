class Room:
    
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.users = []
        users.append(admin)
        

    def getRoom(self):
        room = {
            "name": self.name,
            "admin": self.admin,
            "users": self.users
        }
        return room

    @property
    def name(self):
        return self.name

    @property
    def admin(self):
        return self.admin

    @property
    def users(self):
        return self.isLogged

    @users.setter
    def users(self, user):
        self.users.append(user)
