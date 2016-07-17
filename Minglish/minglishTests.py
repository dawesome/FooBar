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
        words = ['ca', 'cc', 'da']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'acd')

    def test_manyRepeats(self):
        words = ['c', 'cac', 'cb', 'bcc', 'ba']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'cab')

    # ca, cc, da, dc  -> facts = 'cd', 'ac' => acd
    # eq_(minglishlesson.answer(['c', 'cac', 'cb', 'bcc', 'ba']), 'cab')

class factTests(unittest.TestCase):
    def test_factsCreatsTrivialFact(self):
        facts = minglish.makeFacts(['a', 'b'])
        self.assertEqual(facts, ['ab'])

    def test_factsRepeatedFirstLetters(self):
        facts = minglish.makeFacts(['ac', 'aa'])
        self.assertEqual(facts, ['ca'])

    def test_joinFacts(self):
        alphabet = minglish.joinFacts(['cd', 'ac'])
        self.assertEqual(alphabet, 'acd')

class stressTess(unittest.TestCase):
    def test_makeFacts(self):
        words = []
        for x in xrange(50):
            words.append('a' + chr(ord('a') + x) * 49)
        print timeit.timeit(lambda:minglish.makeFacts(words), number=1)

    def test_joinFacts(self):
        words = []
        for x in xrange(50):
            words.append('a' + chr(ord('a') + x) * 49)
        facts = minglish.makeFacts(words)
        print timeit.timeit(lambda:minglish.joinFacts(facts), number=1)

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