def displayColor(color):
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
    return '\u001B[2J'


def setTitle(title):
    title = displayColor('magenta') + f'\n        {title}\n'
    title += '        ' + '-' * 30 + '\n\n' + displayColor('white')
    return title


def errorMsg(message):
    return displayColor('red') + message + '\n' + displayColor('white')


def successMsg(message):
    return displayColor('green') + message + '\n' + displayColor('white')


def unknownCmdMsg():
    unknownCmdMsg = '\n' + errorMsg('unknown command')
    unknownCmdMsg += 'please use "help" to learn more about commands\n'
    return unknownCmdMsg


def tooManyArgs(numArgs = 0):

    if numArgs == 0:
        tooManyArgs = '\n' + errorMsg('client request does not accept additional arguments for this command')
    else:
        tooManyArgs = '\n' + errorMsg('client request does not accept more than ' + str(numArgs) + ' arguments for this command')
        
    tooManyArgs += 'please use "help" to learn more about commands\n'
    return tooManyArgs


def missingArgs():
    missingArgs = '\n' + errorMsg('client request needs additional arguments for this command')
    missingArgs += 'please use "help" to learn more about commands\n'
    return missingArgs


def unknownArgMsg():
    unknownArgMsg = '\n' + errorMsg('unknown arguments for this command')
    unknownArgMsg += 'please use "help" to learn more about commands\n'
    return unknownArgMsg