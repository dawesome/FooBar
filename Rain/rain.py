class Hutch():

    def maxHeight(self):
        return max(self.stackList)

    def printStack(self):
        printedStack = ""
        for height in xrange (self.maxHeight(), 0, -1):
            for stackIter in xrange (len(self.stackList)):
                if self.stackList[stackIter] >= height:
                    printedStack += "X"
                else:
                    printedStack += "."
            printedStack += "\n"

        for stackIter in xrange(len(self.stackList)):
            printedStack += str(self.stackList[stackIter])
        printedStack += "\n"

        return printedStack

    def answer(self, stackList):
        self.stackList = stackList
        start, end = self.findStartAndEndIndex(stackList)


        standingWater = 0
        lastHighest = 0
        lastHighestIndex = 0
        for x in xrange(start, end):
            if self.stackList[x] > lastHighest:
                lastHighest = self.stackList[x]
                lastHighestIndex = x
            elif self.stackList[x] < lastHighest:
                standingWater += lastHighest - self.stackList[x]
        if lastHighest > self.stackList[end]:
            standingDifference = (lastHighest - self.stackList[end]) * (x - lastHighestIndex)
            standingWater -= standingDifference


        return standingWater

    def findStartAndEndIndex(self, stacklist):
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