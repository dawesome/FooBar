def printStack(stackList):
    printedStack = ""
    for height in xrange (max(stackList), 0, -1):
        for stackIter in xrange (len(stackList)):
            if stackList[stackIter] >= height:
                printedStack += "X"
            else:
                printedStack += "."
        printedStack += "\n"

    for stackIter in xrange(len(stackList)):
        printedStack += str(stackList[stackIter])
    printedStack += "\n"

    return printedStack

def answer(stackList):
    # self.stackList = stackList
    start, end = findStartAndEndIndex(stackList)


    standingWater = 0
    lastHighest = 0
    lastHighestIndex = 0
    for x in xrange(start, end):
        if stackList[x] > lastHighest:
            lastHighest = stackList[x]
            lastHighestIndex = x
        elif stackList[x] < lastHighest:
            standingWater += lastHighest - stackList[x]
    if lastHighest > stackList[end]:
        standingDifference = (lastHighest - stackList[end]) * (x - lastHighestIndex)
        standingWater -= standingDifference
    return standingWater

def findStartAndEndIndex(stacklist):
    startHeight = 0
    endHeight = 0
    for x in xrange(len(stacklist) - 1):
        if stacklist[x] > stacklist[x+1]:
            startHeight = x
            break

    # could early out here if startheight = 0?

    for x in xrange(len(stacklist) - 1, 0, -1):
        if stacklist[x] > stacklist[x-1]:
            endHeight = x
            break

    return startHeight, endHeight