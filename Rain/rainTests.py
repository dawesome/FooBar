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

    
