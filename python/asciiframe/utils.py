def getLastLine(text: str) -> str:
    lastLinePosition = 0
    count = 0

    for i in text:
        if i == '\n':
            lastLinePosition = count
        count += 1

    return text[lastLinePosition:]
