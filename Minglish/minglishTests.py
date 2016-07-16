import unittest
import minglish

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

    @unittest.skip
    def test_haveToUseBefore(self):
        words = ['aa', 'aa', 'acce', 'adec']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'acde')

    def test_repeatFirstLetters(self):
        words = ['ca', 'cc', 'da']
        alphabet = minglish.answer(words)
        self.assertEqual(alphabet, 'acd')

    # eq_(minglishlesson.answer(['c', 'cac', 'cb', 'bcc', 'ba']), 'cab')
    # eq_(minglishlesson.answer(['y', 'z', 'xy']), 'yzx')
    # eq_(minglishlesson.answer(['ba', 'ab', 'cb']), 'bac')

class factTests(unittest.TestCase):
    def test_factsCreatsTrivialFact(self):
        facts = minglish.makeFacts(['a', 'b'])
        self.assertEqual(facts, ['ab'])

    def test_factsRepeatedFirstLetters(self):
        facts = minglish.makeFacts(['ac', 'aa'])
        self.assertEqual(facts, ['ca'])

class treeTests(unittest.TestCase):
    def setUp(self):
        self.root = minglish.Node('m')

    def test_canFindRoot(self):
        self.assertEqual(minglish.findInTree(self.root, 'm').value, 'm')

    def test_findReturnsNoneWhenValueNotInTree(self):
        self.assertEqual(minglish.findInTree(self.root, 'e'), None)

    def test_findReturnsLeftNode(self):
        node = minglish.Node('a')
        self.root.left = node
        self.assertEqual(minglish.findInTree(self.root, 'a'), node)

    def test_findReturnsRightNode(self):
        node = minglish.Node('p')
        self.root.right = node
        self.assertEqual(minglish.findInTree(self.root, 'p'), node)

    def test_canInsertAfter(self):
        minglish.insertNode(self.root, 'p', 'm', before=False)
        self.assertEqual(self.root.right.value, 'p')

    def test_canInsertBefore(self):
        minglish.insertNode(self.root, 'a', 'm', before=True)
        self.assertEqual(self.root.left.value, 'a')

    def test_insertOnSelf_AddsNoNodes(self):
        minglish.insertNode(self.root, 'm', 'm')
        self.assertEqual(self.root.left, None)
        self.assertEqual(self.root.right, None)

    def test_insertingSameValue_AddsNoNodes(self):
        minglish.insertNode(self.root, 'a', 'm', before=True)
        minglish.insertNode(self.root, 'p', 'm', before=False)
        minglish.insertNode(self.root, 'a', 'p', before=True)
        self.assertEqual(self.root.left.value, 'a')
        self.assertEqual(self.root.right.value, 'p')
        self.assertEqual(self.root.right.left, None)

    def test_makeInOrderList(self):
        self.root = minglish.Node('8')
        minglish.insertNode(self.root, '4', '8', before=True)
        minglish.insertNode(self.root, '9', '8', before=False)
        minglish.insertNode(self.root, '2', '4', before=True)
        minglish.insertNode(self.root, '5', '4', before=False)
        minglish.insertNode(self.root, '6', '5', before=False)
        inOrderList = []
        minglish.makeInOrderList(self.root, inOrderList)
        self.assertEqual(''.join(inOrderList), '245689')

class binarySearchTreeTests(unittest.TestCase):
    def test_insertOnNull(self):
        root = minglish.insert(None, 8)
        self.assertEqual(root.value, 8)

    def test_insertMany(self):
        root = minglish.insert(None, '8')
        root = minglish.insert(root, '9')
        root = minglish.insert(root, '2')
        root = minglish.insert(root, '4')
        root = minglish.insert(root, '6')
        root = minglish.insert(root, '3')
        root = minglish.insert(root, '1')
        root = minglish.insert(root, '7')
        inOrderList = []
        minglish.makeInOrderList(root, inOrderList)
        self.assertEqual(''.join(inOrderList), '12346789')

    def test_insertLetters(self):
        root = minglish.insert(None, 'd')
        root = minglish.insert(root, 'a')
        root = minglish.insert(root, 'e')
        root = minglish.insert(root, 'b')
        root = minglish.insert(root, 'o')
        root = minglish.insert(root, 'p')
        root = minglish.insert(root, 'z')
        root = minglish.insert(root, 'q')
        inOrderList = []
        minglish.makeInOrderList(root, inOrderList)
        self.assertEqual(''.join(inOrderList), 'abdeopqz')

    def test_insertWithCompare(self):
        alphabet = ['abcdefghijklmnopqrstuvwxyz']
        root = minglish.insert(None, 'd', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'a', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'e', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'b', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'o', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'p', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'z', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        root = minglish.insert(root, 'q', comparitor=minglish.compareLetters, comparitorFacts=alphabet)
        inOrderList = []
        minglish.makeInOrderList(root, inOrderList)
        self.assertEqual(''.join(inOrderList), 'abdeopqz')
