from src.models.Room import Room
import json

class RoomRepository:

    def __init__(self):
        pass


    def fetchAll(self):   
        with open("src/data/rooms.json", "r") as file:
            data = json.load(file) 
        
            return data


    def findByName(self, name):   
        with open("src/data/rooms.json", "r") as file:
            data = json.load(file) 
        
            for room in data:
                if room['name'] == name: 
                    return room 

        return None


    def save(self, room):
        room = room.getRoom()
        with open("src/data/rooms.json", "r") as file:
            data = json.load(file) 
            data.append(room) 

        with open("src/data/rooms.json", "w") as file:
            dataString = json.dumps(data, indent = 4)
            file.write(dataString)


    def update(self, room): 
        name = room['name']

        with open("src/data/rooms.json", "r") as file:
            data = json.load(file)
        print(data)
        print(room)
        lenght = len(data)
        for i in range(lenght):
            if data[i]['name'] == name:
                data[i] = room

        print(data)
        with open("src/data/rooms.json", "w") as file:
            #dataString = json.dumps(data, indent = 4) 
            file.write(data)

        print(data)
        


    def delete(self, room): 
        name = room.name

        with open("src/data/rooms.json", "r") as file:
            data = json.load(file) 
    
        lenght = len(data)
        for i in range(lenght): 
            if data[i]['name'] == name:
                data.pop(i)
                break

        with open("src/data/rooms.json", "w") as file:
            dataString = json.dumps(data, indent = 4)
            file.write(dataString)