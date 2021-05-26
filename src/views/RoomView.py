from src.middlewares.display import *
import src.views.UserView as userView
from src.models.UserRepository import *

def renderOne(room):
    userRepository = UserRepository()

    name = displayColor('yellow') + room['name'] + displayColor('white')

    users = userRepository.fetchAll()
    userList = displayColor('magenta') + ''
    if len(users) != 0:
        i = 0
        for user in users:
            if user['room'] == room['name'] and i == 0:
                userList += user['username'] + '\n'
                i += 1
            elif user['room'] == room['name'] and i > 0:
                userList += '               ' + user['username'] + '\n'

    userList += displayColor('white') + ''

    room = f"""
        name: {name}
        users: {userList}
    """
    return room


def renderMany(rooms):
    roomList = ""
    for i in range(len(rooms)):
        roomList += renderOne(rooms[i])
        roomList += '\n'

    return roomList
