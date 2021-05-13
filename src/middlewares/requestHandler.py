from src.middlewares.display import *
from src.controllers.UserController import UserController
from src.controllers.RoomController import RoomController
import src.views.UserView as userView
import src.views.RoomView as roomView

def requestHandler(request):
    userController = UserController()
    roomController = RoomController()
    request = request.split()

    #print(request)
    if request[0] == 'clear':
        return clearScreen()

    if request[0] == 'exit':
        return 'exit'

    # if request[0] == 'update':
    #     if request[1] == 'username':

    if request[0] == 'uindex':
        users = userController.index()
        print(users)
        title = displayColor('magenta') + '\n        all users\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + userView.renderMany(users)
        return response

    if request[0] == 'ulindex':
        users = userController.index('online')
        print(users)
        title = displayColor('magenta') + '\n        online users\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + userView.renderMany(users)
        return response

    if request[0] == 'ushow':
        username = request[1]
        user = userController.show(username)
        print(user)
        title = displayColor('magenta') + '\n        user\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + userView.renderOne(user)
        return response





    if request[0] == 'rindex':
        rooms = roomController.index()
        print(rooms[0]['users'])
        title = displayColor('magenta') + '\n        all rooms\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + roomView.renderMany(rooms)
        return response

    if request[0] == 'rshow':
        name = request[1]
        room = roomController.show(name)
        print(room)
        title = displayColor('magenta') + '\n        room\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + roomView.renderOne(room)
        return response

    





    return request[0]