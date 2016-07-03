import unittest
import rain

class RainTest(unittest.TestCase):

    def setUp(self):
        self.hutch = rain.Hutch()

    def test_canGetMaxHeight(self):
        self.hutch.answer([5])
        self.assertEqual(5, self.hutch.maxHeight())

        self.hutch.answer([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(5, self.hutch.maxHeight())

    def test_canPrintStack(self):
        self.hutch.answer([1,4,2,5,1,2,3])
        printedStack = self.hutch.printStack()

    def test_printOneColumnStack(self):
        self.hutch.answer([2])
        printedStack = self.hutch.printStack()
        self.assertEqual(printedStack, "X\nX\n2\n")

        self.hutch.answer([1, 4, 2, 5, 1, 2, 3])
        printedStack = self.hutch.printStack()
        self.assertEqual(printedStack, "...X...\n.X.X...\n.X.X..X\n.XXX.XX\nXXXXXXX\n1425123\n")

    def test_canCallAnswer(self):
        self.hutch.answer([2])

    def test_equalTowers(self):
        answer = self.hutch.answer([3,1,3])
        self.assertEqual(answer, 2)

    def test_shorterThenHigher(self):
        answer = self.hutch.answer([2,1,3])
        self.assertEqual(answer, 1)

    def test_higherThenShorter(self):
        answer = self.hutch.answer([3,1,2])
        self.assertEqual(answer, 1)

    def test_degenerateAnswer(self):
        answer = self.hutch.answer([1,2,3,2,1])
        self.assertEqual(answer, 0)

    def test_firstExample(self):
        answer = self.hutch.answer([1,4,2,5,1,2,3])
        self.assertEqual(answer, 5)

    def test_findStartAndEndIndex(self):
        start, end = self.hutch.findStartAndEndIndex([4,1,3])
        self.assertEqual(start, 0)
        self.assertEqual(end, 2)

        start, end = self.hutch.findStartAndEndIndex([1, 4, 2, 5, 1, 2, 3])
        self.assertEqual(start, 1)
        self.assertEqual(end, 6)

        start, end = self.hutch.findStartAndEndIndex([1,2,3,2,1])
        self.assertEqual(start, 2)
        self.assertEqual(end, 2)

