from utils import getLastLine


def addFrame(originText: str, lineCount: int) -> str:
    splitedText = originText.split(sep=' ')
    framedText = ""

    framedText += '+' + '-' * (lineCount - 2) + '+\n'
    framedText += '|' + ' ' * (lineCount - 2) + '|\n'

    for i in range(len(splitedText)):
        if len(getLastLine(framedText)) == 1:
            framedText += '| '

        elemLength = len(splitedText[i])

        if elemLength <= lineCount - 2 - len(getLastLine(framedText)):
            framedText += splitedText[i] + ' '
        else:
            framedText += ' ' * (lineCount - len(getLastLine(framedText))) + '|\n'

    framedText += ' ' * (lineCount - len(getLastLine(framedText))) + '|\n'
    framedText += '|' + ' ' * (lineCount - 2) + '|\n'
    framedText += '+' + '-' * (lineCount - 2) + '+\n'

    return framedText


print(addFrame("text " * 45, 50))
