from src.middlewares.display import *

def renderOne(user):
    username = displayColor('cyan') + user['username'] + displayColor('white')

    if user['isLogged']:
        status = displayColor('green') + 'online' + displayColor('white')
    else:
        status = displayColor('red') + 'offline' + displayColor('white')

    if user['room'] == "":
        room = "none"
    else:
        room = user['room']

    user = f"""
          username: {username}
          status: {status}
          actual room: {room}
    """
    return user


def renderMany(users):
    userList = ""
    for i in range(len(users)):
        userList += renderOne(users[i])
        userList += '\n'

    return userList
