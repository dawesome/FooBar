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
    return calculateWaterInStack(stackList)

def calculateWaterInStack(stacklist):
    pairs = findAllPairs(stacklist)
    water = 0
    for pair in pairs:
        water += calculateWaterInPair(stacklist, pair)
    return water

def calculateWaterInPair(stacklist, pair):
    water = 0
    highestTowerIndex = max(pair)
    highestTowerHeight = stacklist[highestTowerIndex]
    for x in xrange(pair[0], pair[1]):
        water += highestTowerHeight - stacklist[x]
    return water

def findAllPairs(stackList):
    pairs = list()
    finished = False
    index = 0
    while len(stackList) > 1 and not finished:
        first, second, finished = findTowerPair(stackList)
        first += index
        second += index
        index = second
        pairs.append((first, second))
        stackList = stackList[second:]
    return pairs


def findTowerPair(stackList):
    lookedBackwards = False
    leftIndex  = findFirstNonIncreasingIndex(stackList)
    if leftIndex is not None:
        rightIndex = findNextHighestIndex(stackList[leftIndex + 1:], stackList[leftIndex], leftIndex + 1)
        if rightIndex is None:
            rightIndex = findPreviousHighestIndex(stackList, stackList[len(stackList) -1], stackList[leftIndex])
            lookedBackwards = True
    else:
        rightIndex = len(stackList) - 1
        leftIndex  = findPreviousHighestIndex(stackList, stackList[len(stackList) - 1], stackList[len(stackList) - 1])
        lookedBackwards = True
    return leftIndex, rightIndex, lookedBackwards

def findFirstNonIncreasingIndex(stackList):
    for x in xrange(0, len(stackList)):
        if x + 1 < len(stackList) and stackList[x] > stackList[x + 1]:
            return x
    return None

def findNextHighestIndex(stackList, highestPoint, addToIndex=0):
    for x in xrange(len(stackList)):
        if stackList[x] >= highestPoint:
            if x < len(stackList) - 1 and stackList[x] <= stackList[x+1]:
                continue
            return x + addToIndex
    return None

def findPreviousHighestIndex(stackList, highestPoint, pairedTowerHeight=-1):
    for x in xrange(len(stackList) - 1, -1, -1):
        if pairedTowerHeight > 0:
            if stackList[x] > highestPoint or stackList[x] >= pairedTowerHeight:
                return x
        else:
            if stackList[x] > highestPoint:
                return x
    return None

def findLeftStartIndex(stackList):
    # Find the first index of the list where the next element is decreasing
    for x in xrange(len(stackList) - 1):
        if stackList[x] > stackList[x+1]:
            return x
    return len(stackList) - 1

def findRightStartIndex(stackList):
    # Find the first index on the list starting from the right where the next element is non-increasing
    for x in xrange(len(stackList) - 1, -1, -1):
        if stackList[x-1] < stackList[x]:
            return x
    return 0
