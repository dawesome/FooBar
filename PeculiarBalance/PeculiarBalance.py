import math
import itertools
import timeit
import unittest

class TestTernary(unittest.TestCase):
    def test_toTernary(self):
        self.assertEqual(ternary(0), '0')
        self.assertEqual(ternary(1), '1')
        self.assertEqual(ternary(2), '2')
        self.assertEqual(ternary(3), '10')
        self.assertEqual(ternary(4), '11')
        self.assertEqual(ternary(5), '12')
        self.assertEqual(ternary(6), '20')
        self.assertEqual(ternary(9), '100')

class TestBalanced(unittest.TestCase):
    def test_toBalanced(self):
        self.assertEqual(balancedTernaryFromTernary('0'), '-')
        self.assertEqual(balancedTernaryFromTernary('22'), 'R-L')

class RunningAverageTimer():
    def __init__(self):
        self.times = []
        self.t0 = 0.0
        self.t1 = 0.0

    def start(self):
        self.t0 = timeit.default_timer()

    def stop(self):
        self.t1 = timeit.default_timer()
        self.times.append(self.t1 - self.t0)

    def getAverage(self):
        if len(self.times) > 0:
            return sum(self.times) / len(self.times)
        else:
            return 0

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def balancedTernaryFromTernary(tern):
    tern = tern[::-1]
    balanced = []
    carry = 0

    for n in tern:
        intVal = int(n) + carry
        if intVal == 0:
            balanced.append('-')
            carry = 0
        elif intVal == 1:
            balanced.append('L')
            carry = 0
        elif intVal == 2:
            balanced.append('R')
            carry = 1
        elif intVal == 3:
            balanced.append('-')
            carry = 1

    if carry == 1:
        balanced.append('L')
    return ''.join(balanced)[::-1]


def findClosestPowerOf3(x):
    power = 0
    while math.pow(3, power) < x:
        power += 1

    print "Nearest power of 3 to " + str(x) + " is " + str(power)
    nextGreatestPower = math.pow(3, power)
    nextLowerPower    = math.pow(3, power - 1)
    return nextGreatestPower, nextLowerPower

def IsPowerOf3(x):
    return math.log(x, 3).is_integer()

def findLeftAndRightHandWeights(x):
    total = x

    while True:
        # for powIter in range(1, len(powersOf3) + 1):
        for powIter in range(len(powersOf3) + 1, 0, -1):
            # firstComboTimer.start()
            firstCombinations = [list(n) for n in itertools.combinations(powersOf3, powIter)]
            # firstComboTimer.stop()
            # print firstCombinations
            for entry in firstCombinations:
                leftoverEntries = [n for n in powersOf3 if n not in entry]
                for secondIter in range(0, len(leftoverEntries)):
                    # secondComboTimer.start()
                    secondCombinations = [list(n) for n in itertools.combinations(leftoverEntries, secondIter)]
                    # secondComboTimer.stop()
                    for secondEntry in secondCombinations:
                        #print "Checking " + str(entry) + ", " + str(secondEntry)
                        if sum(entry) + x == sum(secondEntry):
                            return entry, secondEntry
                        elif sum(secondEntry) + x == sum(entry):
                            return secondEntry, entry
        # powerAppenderTimer.start()
        powersOf3.append(math.pow(3, len(powersOf3)))
        # powerAppenderTimer.stop()


def oldAnswer(x):
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
firstComboTimer = RunningAverageTimer()
secondComboTimer = RunningAverageTimer()
powerAppenderTimer = RunningAverageTimer()

def answer(x):
    return list(balancedTernaryFromTernary(ternary(x)))

# print answer(2)
# print answer(7)
# print answer(8)

# for x in range(1, 10):
for x in xrange(1, 1000000001):
     thisAnswer = answer(x)
     print str(x) + ": " + str(thisAnswer)
    # if x % 1000 == 0:
    #     print "First combo:  " + str(firstComboTimer.getAverage())
    #     print "Second combo: " + str(secondComboTimer.getAverage())
    #     print "Powers:       " + str(powerAppenderTimer.getAverage())
