from src.middlewares.display import *
from src.controllers.UserController import UserController
from src.controllers.RoomController import RoomController
from src.models.RoomRepository import *
import src.views.UserView as userView
import src.views.RoomView as roomView
    

def requestHandler(request, account, conn, clients):
    userController = UserController()
    roomController = RoomController()
    roomRepository = RoomRepository()
    request = request.split()


    if request[0] == 'clear':
        
        if len(request) > 1:
            return tooManyArgs()

        return clearScreen()


    if request[0] == 'exit':

        if len(request) > 1:
            return tooManyArgs()

        return 'exit'

    if request[0] == 'help':

        if len(request) > 1:
            return tooManyArgs()

        return helpMsg()

    
    if request[0] == 'login':

        if len(request) > 1:
            return tooManyArgs()

        return 'login'

    
    if request[0] == 'logout':

        if len(request) > 1:
            return tooManyArgs()

        return 'logout'


    if request[0] == 'uindex':
        if len(request) > 1:
            return tooManyArgs(1)

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


    if request[0] == 'ulindex':

        if len(request) > 1:
            return tooManyArgs(1)

        users = userController.index('online')
        if users == 'no online users':
            return errorMsg('no online users')

        response = setTitle('online users') + userView.renderMany(users)
        return response


    if request[0] == 'ushow':

        if len(request) > 2:
            return tooManyArgs(2)

        if len(request) < 2:
            return missingArgs()

        username = request[1]
        user = userController.show(username)
        
        if user == 'user not found':
            return errorMsg('user not found')

        response = setTitle('user') + userView.renderOne(user)
        return response





    if request[0] == 'rindex':

        if len(request) > 1:
            return tooManyArgs(1)

        rooms = roomController.index()
        
        response = setTitle('all rooms') + roomView.renderMany(rooms)
        return response

    if request[0] == 'rshow':

        if len(request) > 2:
            return tooManyArgs(2)

        if len(request) < 2:
            return missingArgs()

        name = request[1]
        room = roomController.show(name)
        print(room)
        title = displayColor('magenta') + '\n        room\n'
        title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
        response = title + roomView.renderOne(room)
        return response



    if request[0] == 'join':

        if len(request) > 2:
            return tooManyArgs(2)

        if len(request) < 2:
            return missingArgs()

        name = request[1]
        room = roomController.show(name)

        if room == errorMsg('room not found'):
            return errorMsg('room not found')

        if account.user == '':
            return errorMsg('you need to log in to join a room')

        return 'join ' + name 


    return unknownCmdMsg()
