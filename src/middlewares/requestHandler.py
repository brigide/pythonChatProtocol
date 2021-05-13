from src.middlewares.display import *

def requestHandler(request):
    request = request.split()

    #print(request)
    if request[0] == 'clear':
        return clearScreen()

    if request[0] == 'exit':
        return 'exit'


    return request[0]