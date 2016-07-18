import unittest
import minglish
import timeit

class answerTests(unittest.TestCase):
    def test_canCallAnswer(self):
        minglish.answer([])

    def test_firstGivenCase(self):
        words = ["y", "z", "xy"]
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, "yzx")

    def test_secondGivenCase(self):
        words = ["ba", "ab", "cb"]
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'bac')

    def test_letterOnlyInSecondPlace(self):
        words = ['bb', 'be', 'br']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'ber')

    def test_firstLetterNotEnough(self):
        words = ['be', 'bb', 'br']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'ebr')

    def test_repeatFirstLetters(self):
        words = ['ca', 'cc', 'da', 'dc']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'acd')

    def test_manyRepeats(self):
        words = ['c', 'cac', 'cb', 'bcc', 'ba']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'cab')

    def test_factAfterReapeats(self):
        words = ['a', 'bb', 'bbr', 'bbs', 'bq', 'bre', 'cr', 'ee', 'r']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'abceqrs')


class graphTests(unittest.TestCase):
    def test_makeGraph(self):
        graph = minglish.Graph()
        graph.addNode('a')
        graph.addNode('b')
        graph.nodes['a'].addEdge('b')
        self.assertEqual(len(graph.nodes), 2)
        self.assertEqual(graph.nodes['a'].edges, ['b'])

    def test_makeGraphFromFacts(self):
        facts = ['ab', 'bd', 'cd']
        graph = minglish.makeGraph(facts)
        self.assertEqual(len(graph.nodes), 4)
        self.assertEqual(graph.nodes['a'].edges, ['b'])
        self.assertEqual(graph.nodes['b'].edges, ['d'])
        self.assertEqual(graph.nodes['c'].edges, ['d'])
        self.assertEqual(graph.nodes['d'].edges, [])

    def test_topographicalSort(self):
        facts = ['ab', 'bd', 'abcd']
        graph = minglish.makeGraph(facts)
        alphabet = minglish.topologicalSort(graph)
        self.assertEqual(alphabet, 'abcd')