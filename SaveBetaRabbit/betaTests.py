import unittest
import beta

class AnswerTests(unittest.TestCase):
    def test_canCallAnswer(self):
        food = 7
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
        leftover = beta.answer(food, grid)

    @unittest.skip
    def test_canCallSearch(self):
        food = 0
        start = [0,0]
        beta.search(food, start)

    def test_trivialNoPath(self):
        food = 10
        grid = [[0, 10], [10, 10]]
        leftover = beta.answer(food, grid)
        self.assertEqual(-1, leftover)

    def test_trivialPath(self):
        food = 10
        grid = [[0,1], [1,1]]
        leftover = beta.answer(food, grid)
        self.assertEqual(8, leftover)

    def test_caseOne(self):
        food = 7
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
        leftover = beta.answer(food, grid)
        self.assertEqual(0, leftover)

    def test_caseTwo(self):
        food = 12
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
        leftover = beta.answer(food, grid)
        self.assertEqual(1, leftover)

class NeighborTests(unittest.TestCase):
    def test_getNeighborsZero(self):
        node = beta.LessThanNode(0, [0,0])
        neighbors = beta.getNeighbors(node, gridSize=4)
        self.assertEqual(len(neighbors), 2)
        self.assertEqual(neighbors[0], [1,0])
        self.assertEqual(neighbors[1], [0,1])

    def test_neighborWallRight(self):
        node = beta.LessThanNode(0, [3, 0])
        neighbors = beta.getNeighbors(node, gridSize=4)
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0], [3, 1])

    def test_neighborWallDown(self):
        node = beta.LessThanNode(0, [0, 3])
        neighbors = beta.getNeighbors(node, gridSize=4)
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0], [1, 3])

class RemainderTests(unittest.TestCase):
    def test_simpleRemainder(self):
        grid = [[0, 1], [1, 1]]
        food = 7
        leftover = beta.findSmallestLeftoverFoodForLocation(grid, food, 1, 1)
        self.assertEqual(5, leftover)
