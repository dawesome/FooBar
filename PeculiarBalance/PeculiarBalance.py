import math
import itertools
#import unittest

# class TestFindPowerOf3(unittest.TestCase):
    # def test_findingNext(self):
    #     self.assertEqual(findClosestPowerOf3(1), 1)
    #     self.assertEqual(findClosestPowerOf3(2), 3)
    #     self.assertEqual(findClosestPowerOf3(3), 3)
    #     self.assertEqual(findClosestPowerOf3(4), 3)
    #     self.assertEqual(findClosestPowerOf3(9), 9)
    #     self.assertEqual(findClosestPowerOf3(10), 9)
    #     self.assertEqual(findClosestPowerOf3(24), 27)


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
    powersOf3 = [1]
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
#                        print "Checking " + str(entry) + ", " + str(secondEntry)
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


# print answer(2)
print answer(8)
# for x in range(1, 1000000001):
print answer(7)
for x in range(1, 10):
     print str(x) + ": " + str(answer(x))
