import math
import itertools
import timeit

class RunningAverageTimer():
    def __init__(self):
        self.times = []
        self.t0 = 0
        self.t1 = 0

    def start(self):
        self.t0 = timeit.default_timer

    def stop(self):
        self.t1 = timeit.default_timer
        self.times.append(t1 - t0)

    def getAverage(self):
        return sum(self.times) / len(self.times)

def IsPowerOf3(x):
    return math.log(x, 3).is_integer()

def findLeftAndRightHandWeights(x):
    total = x

    while True:
        for powIter in range(1, len(powersOf3) + 1):
            firstCombinations = [list(n) for n in itertools.combinations(powersOf3, powIter)]
            # print firstCombinations
            for entry in firstCombinations:
                leftoverEntries = [n for n in powersOf3 if n not in entry]
                for secondIter in range(0, len(leftoverEntries)):
                    secondCombinations = [list(n) for n in itertools.combinations(leftoverEntries, secondIter)]
                    for secondEntry in secondCombinations:
                        #print "Checking " + str(entry) + ", " + str(secondEntry)
                        if sum(entry) + x == sum(secondEntry):
                            return entry, secondEntry
                        elif sum(secondEntry) + x == sum(entry):
                            return secondEntry, entry
        powersOf3.append(math.pow(3, len(powersOf3)))

def answer(x):
    leftList, rightList = findLeftAndRightHandWeights(x)
    answerList = list()
    for x in range(0, int(math.log(rightList[-1], 3)) + 1):
        power = math.pow(3, x)
        if power in leftList:
            answerList.append("L")
        elif power in rightList:
            answerList.append("R")
        else:
            answerList.append("-")
    return answerList

powersOf3 = [1, 3, 9, 27]
firstComboTimer = 0.0
secondComboTimer = 0.0
powerAppenderTimer = 0.0

# print answer(2)
#print answer(7)
#print answer(8)

#for x in range(1, 10):
for x in xrange(1, 1000000001):
     print str(x) + ": " + str(answer(x))
