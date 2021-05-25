from src.models.Room import Room
from src.models.RoomRepository import RoomRepository
from src.middlewares.display import *
import json 


class RoomController:
    roomRepository = RoomRepository()

    def __init__(self):
        pass


    def index(self):
        return self.roomRepository.fetchAll()

    
    def show(self, name):
        room = self.roomRepository.findByName(name)

        if room == None:
            return errorMsg('room not found')
        
        return room


    def create(self, room):
        print('cheguei')
        if self.roomRepository.findByName(room.name) != None:
            return errorMsg('room name already in use')

        
        self.roomRepository.save(room)

        return successMsg('room created succefully')

    
    def update(self, room):
        if self.roomRepository.findByName(room.name) == None:
            return errorMsg('room not found')
        
        self.roomRepository.update(room)

        return successMsg('room updated succefully')


    def delete(self, room):
        if self.roomRepository.findByName(room.name) == None:
            return errorMsg('room not found')

        self.roomRepository.delete(room)

        return successMsg('room removed succefully')