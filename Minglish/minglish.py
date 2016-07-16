from collections import OrderedDict

def answer(words):
    # return firstAttempt(words)

    root = None
    factList = makeFacts(words)
    allLetters = set(''.join(x for x in factList))

#     while currentAlphabetizedList:
# #        root = insertLetters(currentAlphabetizedList, root)
#         currentAlphabetizedList, words = sliceFirstLetters(words)
#         factList.append(currentAlphabetizedList)
#         allLetters = allLetters.union(set(currentAlphabetizedList))

    # This is the BST attempt
    # for letter in allLetters:
    #     root = insert(root, letter, comparitor=compareLetters, comparitorFacts=factList)

    # inOrderList = []
    # makeInOrderList(root, inOrderList)
    # return ''.join(inOrderList)

    alphabet = joinFacts(factList)
    return alphabet

def makeFacts(words):
    facts = []

    firstLetters = [x[0] for x in words]
    # Find any repeats
    repeatedLetter = ''
    wordsToMakeMoreFactsFrom = []
    for i in xrange(len(firstLetters)):
        if not repeatedLetter or firstLetters[i] != repeatedLetter:
            repeatedLetter = firstLetters[i]
            if len(wordsToMakeMoreFactsFrom) > 1:
                newFacts = makeFacts(wordsToMakeMoreFactsFrom)
                if newFacts:
                    facts.append(newFacts[0])
            wordsToMakeMoreFactsFrom = [words[i][1:]]
            continue
        else:
            wordsToMakeMoreFactsFrom.append(words[i][1:])

    if len(wordsToMakeMoreFactsFrom) > 1:
        newFacts = makeFacts(wordsToMakeMoreFactsFrom)
        if newFacts:
            facts.append(newFacts[0])

    possibleFacts = list(OrderedDict.fromkeys(firstLetters))
    if len(possibleFacts) > 1:
        facts.append(''.join(possibleFacts))
    return facts

def joinFacts(facts):
    while len(facts) > 1:
        firstFact = facts[0]
        for x in xrange(1, len(facts)):
            if firstFact[0] == facts[x][len(facts[x]) - 1]:
                newFact = facts[x] + firstFact[1:]
                facts.remove(facts[x])
                facts.remove(firstFact)
                facts.append(newFact)
                break
            elif firstFact[len(firstFact) - 1] == facts[x][0]:
                newFact = firstFact + facts[x][1:]
                facts.remove(facts[x])
                facts.remove(firstFact)
                facts.append(newFact)
                break
    return ''.join(facts)

def insertLetters(currentAlphabetizedList, root):
    if currentAlphabetizedList:
        lastLetter = currentAlphabetizedList[0]
        if root is None:
            root = Node(lastLetter)
        elif len(currentAlphabetizedList) > 1:
            insertNode(root, lastLetter, currentAlphabetizedList[1], before=True)

        for letterIndex in range(1, len(currentAlphabetizedList)):
            insertNode(root, currentAlphabetizedList[letterIndex], lastLetter, before=False)
            lastLetter = currentAlphabetizedList[letterIndex]
    return root


def sliceFirstLetters(words):
    currentAlphabetizedList = []
    for x in range (len(words)):
        currentAlphabetizedList.append(words[x][0])
        words[x] = words[x][1:]
    return currentAlphabetizedList, filter(None, words)

def firstAttempt(words):
    alphabet = []
    leftoverWords = []
    for word in words:
        if word[0] not in alphabet:
            alphabet.append(word[0])
            word = word[1:]
            if word != '':
                leftoverWords.append(word)

                #    while len(leftoverWords) != 0:

    return ''.join(alphabet)

class Node():
    def __init__(self, value):
        self.left  = None
        self.right = None
        self.value = value

def findInTree(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    leftAnswer = findInTree(node.left, value)
    if leftAnswer is not None:
        return leftAnswer
    else:
        return findInTree(node.right, value)

def insertNode(root, valueToInsert, afterValue, before=True):
    if root is None:
        root = Node(valueToInsert)
    elif valueToInsert == afterValue:
        return
    elif findInTree(root, valueToInsert):
        return
    else:
        insertParentNode = findInTree(root, afterValue)
        try:
            if before:
                insertParentNode.left = Node(valueToInsert)
            else:
                insertParentNode.right = Node(valueToInsert)
        except AttributeError as e:
            raise StandardError("hit AttributeError with afterValue = " + afterValue)

def insert(root, value, comparitor=None, comparitorFacts=None):
    if root is None:
        root = Node(value)

    elif root.value > value if comparitor is None else comparitor(root.value, value, comparitorFacts):
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value, comparitor, comparitorFacts)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value, comparitor, comparitorFacts)
    return root

def makeInOrderList(root, list):
    if root is None:
        return

    if root.left:
        makeInOrderList(root.left, list)
    list.append(root.value)
    if root.right:
        makeInOrderList(root.right, list)

def compareLetters(first, second, facts):
    def internalCompare(first, second):
        fact = [x for x in facts if first in x and second in x]
        return fact[0].index(first) > fact[0].index(second)

    return internalCompare(first, second)