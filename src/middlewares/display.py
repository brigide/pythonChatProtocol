def displayColor(color):
    """
        method to choose color to display on client
    """
    color = color.upper()

    if color == 'BLACK':
        return '\u001b[30m'

    if color == 'RED':
        return '\u001b[31m'

    if color == 'GREEN':
        return '\u001b[32m'

    if color == 'YELLOW':
        return '\u001b[33m'

    if color == 'BLUE':
        return '\u001b[34m'

    if color == 'MAGENTA':
        return '\u001b[35m'

    if color == 'CYAN':
        return '\u001b[36m'

    return '\u001b[37m'


def clearScreen():
    """
        method to clear client's screen
    """
    return '\u001B[2J'


def setTitle(title):
    """
        method to set a title on client
    """
    title = displayColor('magenta') + f'\n        {title}\n'
    title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    return title


def setPrefix(account):
        """
            prefix is the room and user resume shown in client
            to indicade current user and room
            default is 'none@unkown', where none is for room and
            unknown for user
        """
        if account.user == '':
            room = displayColor('cyan') + 'none'
            username = displayColor('cyan') + 'unknown'  
        else:
            if account.user.room == '':
                room = displayColor('cyan') + 'none'
            else:
                room = displayColor('magenta') + account.user.room

            username = displayColor('yellow') + account.user.username

        prefix = room + '@' + username + displayColor('white') + '> '

        return prefix


def errorMsg(message):
    """
        method to set an error message
    """
    return displayColor('red') + message + '\n' + displayColor('white')


def successMsg(message):
    """
        method to set a success message
    """
    return displayColor('green') + message + '\n' + displayColor('white')


def unknownCmdMsg():
    """
        method to set a message in response for unknow command
    """
    unknownCmdMsg = '\n' + errorMsg('unknown command')
    unknownCmdMsg += 'please use "help" to learn more about commands\n'
    return unknownCmdMsg


def tooManyArgs(numArgs = 0):
    """
        method to set a response for incorrect arguments for a commando
    """

    if numArgs == 0:
        tooManyArgs = '\n' + errorMsg('client request does not accept additional arguments for this command')
    else:
        tooManyArgs = '\n' + errorMsg('client request does not accept more than ' + str(numArgs) + ' arguments for this command')
        
    tooManyArgs += 'please use "help" to learn more about commands\n'
    return tooManyArgs


def missingArgs():
    """
        method to set a response for incorrect arguments for a commando
    """
    missingArgs = '\n' + errorMsg('client request needs additional arguments for this command')
    missingArgs += 'please use "help" to learn more about commands\n'
    return missingArgs


def unknownArgMsg():
    """
        method to set a response for incorrect arguments for a commando
    """
    unknownArgMsg = '\n' + errorMsg('unknown arguments for this command')
    unknownArgMsg += 'please use "help" to learn more about commands\n'
    return unknownArgMsg


def helpMsg():
    message = setTitle('all commands')
    message += displayColor('cyan') + 'clear: ' + displayColor('white') + 'clear last commands\n'
    message += displayColor('cyan') + 'exit: ' + displayColor('white') + 'close app\n'
    message += '\n'
    message += displayColor('cyan') + 'uindex: ' + displayColor('white') + 'list all users\n'
    message += displayColor('cyan') + 'ulindex: ' + displayColor('white') + 'list all online users\n'
    message += displayColor('cyan') + 'ushow username: ' + displayColor('white') + 'list specific user\n'
    message += '\n'
    message += displayColor('cyan') + 'rindex: ' + displayColor('white') + 'list all rooms\n'
    message += displayColor('cyan') + 'rshow roomname: ' + displayColor('white') + 'list specific room\n'
    message += '\n'
    message += displayColor('cyan') + 'create user: ' + displayColor('white') + 'create new user\n' 
    message += displayColor('cyan') + 'login: ' + displayColor('white') + 'login w/ user\n'
    message += displayColor('cyan') + 'logout: ' + displayColor('white') + 'logout w/ user\n'
    message += '\n'
    message += displayColor('cyan') + 'join roomname: ' + displayColor('white') + 'enter room to chat\n'
    message += displayColor('cyan') + '/exit: ' + displayColor('white') + 'exit current room\n'
    return message