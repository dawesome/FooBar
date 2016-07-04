import unittest
import rain


class SetupTests(unittest.TestCase):
    def test_findLeftStart(self):
        start = rain.findLeftStartIndex([1,4,2,5])
        self.assertEqual(start, 1)

@unittest.skip("skip general tests")
class RainTest(unittest.TestCase):
    def test_canPrintStack(self):
        printedStack = rain.printStack([1,4,2,5,1,2,3])

    def test_printOneColumnStack(self):
        printedStack = rain.printStack([2])
        self.assertEqual(printedStack, "X\nX\n2\n")

        printedStack = rain.printStack([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(printedStack, "...X...\n.X.X...\n.X.X..X\n.XXX.XX\nXXXXXXX\n1425123\n")


    def test_findStartAndEndIndex(self):
        start, end = rain.findStartAndEndIndex([4, 1, 3])
        self.assertEqual(start, 0)
        self.assertEqual(end, 2)

        start, end = rain.findStartAndEndIndex([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(start, 1)
        self.assertEqual(end, 6)

        start, end = rain.findStartAndEndIndex([1, 2, 3, 2, 1])
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)

    def test_pairs_one(self):
        pairs = rain.findAllPairs([3, 1, 2, 5, 1, 2, 4, 3])
        self.assertEqual([(0, 3), (3, 6)], pairs)


    def test_findNextTower(self):
        firstTower = rain.findNextHighestIndex([1, 4, 2, 5], 1)
        self.assertEqual(firstTower, 1)

    def test_findTowerPair_easy(self):
        first, second, finished = rain.findTowerPair([1,4,2,5])
        self.assertEqual(first, 1)
        self.assertEqual(second, 3)

    def test_findTowerPair_none(self):
        first, second, finished = rain.findTowerPair([1,2,3,2,1])
        self.assertEqual(first, 2)
        self.assertEqual(second, 2)
        self.assertTrue(finished)

    def test_findTowerPair_repeated(self):
        first, second, finished = rain.findTowerPair([1,1,2,2,5,5,5,3,5,5,1])
        self.assertEqual(first, 6)
        self.assertEqual(second, 9)
        self.assertTrue(finished)

    def test_findTowerPair_hard(self):
        first, second, finished = rain.findTowerPair([5,3,1,2])
        self.assertEqual(first, 1)
        self.assertEqual(second, 3)
        self.assertTrue(finished)

    def test_findTowerPair_SecondInMultiple(self):
        first, second, finished = rain.findTowerPair([5,1,2,3])
        self.assertEqual(first, 0)
        self.assertEqual(second, 3)

    def test_findPairsDegenerate(self):
        pairs = rain.findAllPairs([1,2,3,2,1])
        self.assertEqual([(2,2)], pairs)

    def test_findPairsSingle(self):
        """this is failing now because the "first index is the first non-decreasing" logic
           (found in test_one) doesn't work for this example.
           5 is a candidate, for sure, but once you find the right tower, you have to
           go back and make sure you get the smallest maximum greater than the minimum tower.

           Or is it a special case?
           if you have 1, 3, 2... you go up from left until you hit a decreasing value.
               -- This is just to throw out the edge that water would fall off from
           but if you have 5, 3, 1, 2, you can't just assume non-decreasing is your left tower
           It's a possible tower (as in 3, 1, 3)
           but then you have to find the right tower first (first value >= candidate tower,
           or right edge), then work back to find the smallest-max-greater-than-minumum
           """
        pairs = rain.findAllPairs([5,3,1,2])
        self.assertEqual([(1,3)], pairs)

    def test_findPairsMultiple(self):
        pairs = rain.findAllPairs([1,4,2,5,1,2,3])
        self.assertEqual([(1,3), (3,6)], pairs)

    def test_waterCalc_one(self):
        water = rain.calculateWaterInStack([1,4,2,5,1,2,3])
        self.assertEqual(water, 5)

    def test_waterCalc_none(self):
        water = rain.calculateWaterInStack([1,2,3,2,1])
        self.assertEqual(water, 0)

@unittest.skip("Skipping answers for now")
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
