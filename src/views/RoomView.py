from src.middlewares.display import *
import src.views.UserView as userView

def renderOne(room):
    name = displayColor('yellow') + room['name'] + displayColor('white')

    admin = displayColor('cyan') + room['admin'] + displayColor('white')

    users = userView.renderMany(room['users'])

    room = f"""
        name: {name}
        admin: {admin}
        users: {users}
    """
    return room


def renderMany(rooms):
    roomList = ""
    for i in range(len(rooms)):
        roomList += renderOne(rooms[i])
        roomList += '\n'

    return roomList
