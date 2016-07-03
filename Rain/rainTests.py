import unittest
import rain

class RainTest(unittest.TestCase):
    def test_canPrintStack(self):
        printedStack = rain.printStack([1,4,2,5,1,2,3])

    def test_printOneColumnStack(self):
        printedStack = rain.printStack([2])
        self.assertEqual(printedStack, "X\nX\n2\n")

        printedStack = rain.printStack([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(printedStack, "...X...\n.X.X...\n.X.X..X\n.XXX.XX\nXXXXXXX\n1425123\n")

    def test_canCallAnswer(self):
        rain.answer([2])

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

    def test_findStartAndEndIndex(self):
        start, end = rain.findStartAndEndIndex([4,1,3])
        self.assertEqual(start, 0)
        self.assertEqual(end, 2)

        start, end = rain.findStartAndEndIndex([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(start, 1)
        self.assertEqual(end, 6)

        start, end = rain.findStartAndEndIndex([1,2,3,2,1])
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)

