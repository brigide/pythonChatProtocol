from src.models.User import User
import json

class UserRepository:

    def __init__(self):
        pass


    def fetchAll(self):   
        with open("src/data/users.json", "r") as file:
            data = json.load(file) 
        
            return data

    def fetchLogged(self):
        with open("src/data/users.json", "r") as file:
            data = json.load(file)

            users = []

            for user in data:
                if user['isLogged'] == True:
                    users.append(user)

        if len(users) == 0:
            return 'no online users'

        return users


    def findByUsername(self, username):   
        with open("src/data/users.json", "r") as file:
            data = json.load(file) 
        
            for user in data:
                if user['username'] == username: 
                    return user 

        return None


    def save(self, user):
        user = user.getUser()
        with open("src/data/users.json", "r") as file:
            #print(user)
            data = json.load(file) 
            data.append(user) 

        with open("src/data/users.json", "w") as file:
            dataString = json.dumps(data, indent = 4)
            file.write(dataString)


    def update(self, user): 
        username = user.username

        with open("src/data/users.json", "r") as file:
            data = json.load(file)
    
        lenght = len(data)
        for i in range(lenght):
            if data[i]['username'] == username:
                data[i] = user.getUser()

        with open("src/data/users.json", "w") as file:
            dataString = json.dumps(data, indent = 4) 
            file.write(dataString)


    def delete(self, user): 
        username = user.username

        with open("src/data/users.json", "r") as file:
            data = json.load(file) 
    
        lenght = len(data)
        for i in range(lenght): 
            if data[i]['username'] == username:
                data.pop(i)
                break

        with open("src/data/users.json", "w") as file:
            dataString = json.dumps(data, indent = 4)
            file.write(dataString)