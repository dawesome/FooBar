def answer(words):
    # return firstAttempt(words)

    root = None
    factList = []
    allLetters = []

    currentAlphabetizedList, words = sliceFirstLetters(words)
    factList.append(currentAlphabetizedList)
    allLetters = set(currentAlphabetizedList)

    while currentAlphabetizedList:
#        root = insertLetters(currentAlphabetizedList, root)
        currentAlphabetizedList, words = sliceFirstLetters(words)
        factList.append(currentAlphabetizedList)
        allLetters = allLetters.union(set(currentAlphabetizedList))


    for letter in allLetters:
        pass # here, need to insert all letters using fact-list comparitors

    inOrderList = []
    makeInOrderList(root, inOrderList)
    return ''.join(inOrderList)


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

def insert(root, value):
    if root is None:
        root = Node(value)
    elif root.value > value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)
    return root

def makeInOrderList(root, list):
    if root is None:
        return

    if root.left:
        makeInOrderList(root.left, list)
    list.append(root.value)
    if root.right:
        makeInOrderList(root.right, list)