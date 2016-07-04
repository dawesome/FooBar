import unittest
import rain


class FindStartPointTests(unittest.TestCase):
    def test_findLeftDegenerate(self):
        start = rain.findLeftStartIndex([])
        self.assertEqual(start, -1)

    def test_findLeftStart(self):
        start = rain.findLeftStartIndex([1,4,2,5])
        self.assertEqual(start, 1)

    def test_findLeftStart_Mountain(self):
        start = rain.findLeftStartIndex([1,2,3,4,5])
        self.assertEqual(start, 4)

    def test_findLeftStart_Descending(self):
        start = rain.findLeftStartIndex([5,4,3,2,1])
        self.assertEqual(start, 0)

    def test_findLeftStart_Repeating(self):
        start = rain.findLeftStartIndex([2,2,3,2])
        self.assertEqual(start, 2)

    def test_findLeftStart_AllRepeating(self):
        start = rain.findLeftStartIndex([1,1,1,1,1])
        self.assertEqual(start, 4)

    def test_findRightStart(self):
        end = rain.findRightStartIndex([1,4,2,5])
        self.assertEqual(end, 3)

    def test_findRightStart_Mountain(self):
        end = rain.findRightStartIndex([1,2,3,4,5])
        self.assertEqual(end, 4)

    def test_findRightStart_Descending(self):
        end = rain.findRightStartIndex([5,4,3,2,1])
        self.assertEqual(end, 0)

    def test_findRightStart_Repeating(self):
        end = rain.findRightStartIndex([2,3,2,2])
        self.assertEqual(end, 1)

    def test_findRightStart_AllRepeating(self):
        end = rain.findRightStartIndex([1,1,1,1,1])
        self.assertEqual(end, 0)

class StripHutchEdgesTests(unittest.TestCase):
    def test_stripLeft(self):
        stripped = rain.stripHutches([1,2,3,2,3])
        self.assertEqual(stripped, [3,2,3])

    def test_stripRight(self):
        stripped = rain.stripHutches([3,2,3,2,1])
        self.assertEqual(stripped, [3,2,3])

    def test_stripBoth(self):
        stripped = rain.stripHutches([1,4,3,4,3,3,2])
        self.assertEqual(stripped, [4,3,4])

    def test_stripNone(self):
        stripped = rain.stripHutches([5,3,1,2])
        self.assertEqual(stripped, [5,3,1,2])

    def test_stripDegenerate(self):
        stripped = rain.stripHutches([1,2,3,2,1])
        self.assertEqual(stripped, [3])

class TowerTests(unittest.TestCase):
    def test_findTowerToRight(self):
        rightIndex = rain.findMatchingTowerToRight([4,2,5], 0)
        self.assertEqual(rightIndex, 2)

    def test_findEqualTowerRight(self):
        rightIndex = rain.findMatchingTowerToRight([3,1,2,3], 0)
        self.assertEqual(rightIndex, 3)

    def test_findNoTowerToRight(self):
        rightIndex = rain.findMatchingTowerToRight([4,3,1,2], 0)
        self.assertIsNone(rightIndex)

    def test_findNoTowerRightDegenerate(self):
        rightIndex = rain.findMatchingTowerToRight([3], 0)
        self.assertIsNone(rightIndex)

    def test_findTowerToLeft(self):
        leftIndex = rain.findMatchingTowerToLeft([5,2,4], 2)
        self.assertEqual(leftIndex, 0)

    def test_findEqualTowerToLeft(self):
        leftIndex = rain.findMatchingTowerToLeft([4,3,2,3,1,4], 5)
        self.assertEqual(leftIndex, 0)

    def test_findNoTowerToLeft(self):
        leftIndex = rain.findMatchingTowerToLeft([1,2,3,5], 3)
        self.assertIsNone(leftIndex)

    def test_findNoTowerLeftDegenerate(self):
        leftIndex = rain.findMatchingTowerToLeft([3], 0)
        self.assertIsNone(leftIndex)

class PairTests(unittest.TestCase):
    def test_findNoPairs(self):
        first, second, stacklist, removedFromLeft = rain.findAndRemoveTowerPair([])
        self.assertEqual(first, -1)
        self.assertEqual(second, -1)

    def test_findTowerPair_fromLeft(self):
        first, second, stackList, removedFromLeft = rain.findAndRemoveTowerPair([1, 4, 2, 5])
        self.assertEqual(first, 1)
        self.assertEqual(second, 3)

    def test_findTowerPair_none(self):
        first, second, stackList, removedFromLeft = rain.findAndRemoveTowerPair([1, 2, 3, 2, 1])
        self.assertIsNone(first)
        self.assertIsNone(second)

    def test_findTowerPair_repeated(self):
        first, second, stackList, removedFromLeft = rain.findAndRemoveTowerPair([1, 1, 2, 2, 5, 5, 5, 3, 5, 5, 1])
        self.assertEqual(first, 6)
        self.assertEqual(second, 8)

    def test_findTowerPair_fromRight(self):
        first, second, stackList, removedFromLeft = rain.findAndRemoveTowerPair([5, 3, 1, 2])
        self.assertEqual(first, 1)
        self.assertEqual(second, 3)

    def test_findTowerPair_SecondInMultiple(self):
        first, second, stackList, removedFromLeft = rain.findAndRemoveTowerPair([5, 1, 2, 3])
        self.assertEqual(first, 0)
        self.assertEqual(second, 3)

class AllPairsTests(unittest.TestCase):
    def test_findPairsDegenerate(self):
        pairs = rain.findAllPairs([1,2,3,2,1])
        self.assertEqual([], pairs)

    def test_findPairsSingle(self):
        pairs = rain.findAllPairs([5,3,1,2])
        self.assertEqual([(1,3)], pairs)

    def test_findPairsMultiple(self):
        pairs = rain.findAllPairs([1,4,2,5,1,2,3])
        self.assertEqual([(1,3), (3,6)], pairs)

    def test_findTowerPair_ThreePairs(self):
        pairs = rain.findAllPairs([8,1,8,7,3,7,2,4])
        self.assertEqual(pairs, [(0,2), (5,7), (3,5)])

class RainTest(unittest.TestCase):
    def test_canPrintStack(self):
        printedStack = rain.printStack([1,4,2,5,1,2,3])

    def test_printOneColumnStack(self):
        printedStack = rain.printStack([2])
        self.assertEqual(printedStack, "X\nX\n2\n")

        printedStack = rain.printStack([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(printedStack, "...X...\n.X.X...\n.X.X..X\n.XXX.XX\nXXXXXXX\n1425123\n")

    def test_pairs_one(self):
        pairs = rain.findAllPairs([3, 1, 2, 5, 1, 2, 4, 3])
        self.assertEqual([(0, 3), (3, 6)], pairs)


class WaterCalcInPairTests(unittest.TestCase):
    def test_waterInPair_one(self):
        water = rain.calculateWaterInPair([3,1,2], (0,2))
        self.assertEqual(water, 1)

    def test_waterCalc_one(self):
        water = rain.calculateWaterInStack([1,4,2,5,1,2,3])
        self.assertEqual(water, 5)

    def test_waterCalc_none(self):
        water = rain.calculateWaterInStack([1,2,3,2,1])
        self.assertEqual(water, 0)

class RainAnswerTests(unittest.TestCase):
    def test_equalTowers(self):
        answer = rain.answer([3,1,3])
        self.assertEqual(answer, 2)

    def test_shorterThenHigher(self):
        answer = rain.answer([2,1,3])
        self.assertEqual(answer, 1)

    def test_higherThenShorter(self):
        answer = rain.answer([3,1,2])
        self.assertEqual(answer, 1)

    def test_degenerateAnswer(self):
        answer = rain.answer([1,2,3,2,1])
        self.assertEqual(answer, 0)

    def test_firstExample(self):
        answer = rain.answer([1,4,2,5,1,2,3])
        self.assertEqual(answer, 5)

    def test_weirdCase(self):
        answer = rain.answer([3, 2, 1, 1, 1, 2, 3])
        self.assertEqual(answer, 1+2+2+2+1)

    def test_one(self):
        answer = rain.answer([3, 1, 2, 5, 1, 2, 4, 3])
        self.assertEqual(answer, 2+1+3+2)

    def test_two(self):
        answer = rain.answer([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(answer, 2+2+1)

    def test_three(self):
        answer = rain.answer([3, 1, 1, 1, 5])
        self.assertEqual(answer, 6)

    def test_four(self):
        answer = rain.answer([3, 1, 2, 2, 1, 3])
        self.assertEqual(answer, 6)

    def test_five(self):
        answer = rain.answer([4, 1, 2, 5, 5, 2, 5])
        self.assertEqual(answer, 3+2+3)

    def test_six(self):
        answer = rain.answer([1, 2, 3, 2, 1])
        self.assertEqual(answer, 0)

    def test_seven(self):
        answer = rain.answer([5, 3, 2, 4, 7, 5, 4, 3])
        self.assertEqual(answer, 2+3+1)

    def test_eight(self):
        answer = rain.answer([1, 2, 2, 2, 2, 1])
        self.assertEqual(answer, 0)

    def test_nine(self):
        answer = rain.answer([3, 1, 1, 4, 1, 2, 1, 3, 2, 1, 1, 5])
        self.assertEqual(answer, (2+2)+(3+2+3+1+2+3+3))

    def test_ten(self):
        answer = rain.answer([1, 2, 3, 1, 2, 1, 1, 5, 3, 1, 2, 1])
        self.assertEqual(answer, (2+1+2+2)+1)

    def test_decreasingValley(self):
        answer = rain.answer([5,3,1,2])
        self.assertEqual(answer, 1)

    def test_increasingValley(self):
        answer = rain.answer([2,1,3,5])
        self.assertEqual(answer, 1)

    def test_manyRepeats(self):
        answer = rain.answer([2,2,2,2,2,2,2,2,1,7,8,9,6,5,5,5,5,5,3,2,1])
        self.assertEqual(answer, 1)

    def test_anotherTestCase(self):
        answer = rain.answer([3, 2, 1, 1, 1, 2, 3])
        self.assertEqual(answer, 1+2+2+2+1)

    def test_repeatedTowers(self):
        answer = rain.answer([1,3,4,5,1,5,5,5,3,2,2,1,2])
        self.assertEqual(answer, 5)