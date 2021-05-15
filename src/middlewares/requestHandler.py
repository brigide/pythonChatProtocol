from src.middlewares.display import *
from src.controllers.UserController import UserController
from src.controllers.RoomController import RoomController
import src.views.UserView as userView
import src.views.RoomView as roomView
    

def requestHandler(request):
    userController = UserController()
    roomController = RoomController()
    request = request.split()


    if request[0] == 'clear':
        
        if len(request) > 1:
            return tooManyArgs()

        return clearScreen()


    if request[0] == 'exit':

        if len(request) > 1:
            return tooManyArgs()

        return 'exit'

    
    if request[0] == 'login':

        if len(request) > 1:
            return tooManyArgs()

        return 'login'

    
    if request[0] == 'logout':

        if len(request) > 1:
            return tooManyArgs()

        return 'logout'


    if request[0] == 'uindex':
        users = userController.index()
        response = setTitle('all users') + userView.renderMany(users)
        return response


    if request[0] == 'create':

        if len(request) < 2:
            return missingArgs()

        if len(request) > 2:
            return tooManyArgs(2)

        if request[1] == 'user':
            return 'create user'

        if request[1] == 'room':
            return 'create room'

        return unknownArgMsg() 

    # if request[0] == 'ulindex':
    #     users = userController.index('online')
    #     print(users)
    #     title = displayColor('magenta') + '\n        online users\n'
    #     title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    #     response = title + userView.renderMany(users)
    #     return response

    # if request[0] == 'ushow':
    #     username = request[1]
    #     user = userController.show(username)
    #     print(user)
    #     title = displayColor('magenta') + '\n        user\n'
    #     title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    #     response = title + userView.renderOne(user)
    #     return response





    # if request[0] == 'rindex':
    #     rooms = roomController.index()
    #     print(rooms[0]['users'])
    #     title = displayColor('magenta') + '\n        all rooms\n'
    #     title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    #     response = title + roomView.renderMany(rooms)
    #     return response

    # if request[0] == 'rshow':
    #     name = request[1]
    #     room = roomController.show(name)
    #     print(room)
    #     title = displayColor('magenta') + '\n        room\n'
    #     title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    #     response = title + roomView.renderOne(room)
    #     return response

    return unknownCmdMsg()