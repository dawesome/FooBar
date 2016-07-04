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
    lowestTowerHeight = min(stacklist[pair[0]], stacklist[pair[1]])
    for x in xrange(pair[0] + 1, pair[1]):
        water += lowestTowerHeight - stacklist[x]
    return water

def findAllPairs(stackList):
    pairs = list()
    finished = False
    index = 0
    while len(stackList) > 1 and not finished:
        first, second, stackList, removedFromLeft = findAndRemoveTowerPair(stackList)
        if first is None:
            return pairs

        first += index
        second += index
        if removedFromLeft:
            index = second
        pairs.append((first, second))
    return pairs


def findAndRemoveTowerPair(stackList):
    removedFromLeft = True
    left, right = findTowerFromLeft(stackList)

    if left is None or right is None:
        left, right = findTowerFromRight(stackList)
        if left is None or right is None:
            left, right = None, None
        else:
            stackList = stackList[:left + 1]
            removedFromLeft = False
    else:
        stackList = stackList[right:]

    return left, right, stackList, removedFromLeft


def findTowerFromLeft(stackList):
    leftTowerIndex = findLeftStartIndex(stackList)
    if leftTowerIndex is not -1:
        rightTowerIndex = findMatchingTowerToRight(stackList, leftTowerIndex)
    else:
        rightTowerIndex = -1
    return leftTowerIndex, rightTowerIndex

def findTowerFromRight(stackList):
    rightTowerIndex = findRightStartIndex(stackList)
    if rightTowerIndex is not -1:
        leftTowerIndex = findMatchingTowerToLeft(stackList, rightTowerIndex)
    else:
        leftTowerIndex = -1
    return leftTowerIndex, rightTowerIndex

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

def stripHutches(stackList):
    startIndex = findLeftStartIndex(stackList)
    endIndex   = findRightStartIndex(stackList)
    return stackList[startIndex:endIndex + 1]

def findMatchingTowerToRight(stackList, leftTowerIndex):
    towerHeight = stackList[leftTowerIndex]
    for x in xrange(leftTowerIndex + 1, len(stackList)):
        if stackList[x] >= towerHeight:
            return x
    return None

def findMatchingTowerToLeft(stackList, rightTowerIndex):
    towerHeight = stackList[rightTowerIndex]
    for x in xrange(rightTowerIndex - 1, -1, -1):
        if stackList[x] >= towerHeight:
            return x
    return None
