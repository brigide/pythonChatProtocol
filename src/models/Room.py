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

    def addUser(self, user):
        self.users.append(user)

    def removeUser(self, user):
        self.users.remove(user)

    def addConn(self, conn):
        self.conns.append(conn)

    def removeConn(self, conn):
        self.conns.remove(conn)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, admin):
        self._admin = admin

    @property
    def users(self):
        return self.users

    @property
    def conns(self):
        return self.conns
