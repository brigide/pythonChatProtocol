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