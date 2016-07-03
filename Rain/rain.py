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