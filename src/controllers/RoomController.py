from src.models.Room import Room
from src.models.RoomRepository import RoomRepository
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
            return 'room not found'
        
        return room


    def create(self, room):
        if self.roomRepository.findByName(room.name) != None:
            return 'room name already in use'

        self.roomRepository.save(room)

        return 'room created succefully'

    
    def update(self, room):
        if self.roomRepository.findByName(room.name) == None:
            return 'room not found'
        
        self.roomRepository.update(room)

        return 'room updated succefully'


    def delete(self, room):
        if self.roomRepository.findByName(room.name) == None:
            return 'room not found'

        self.roomRepository.delete(room)

        return 'room removed succefully'