from collections import OrderedDict
import timeit

def answer(words):
    factList = makeFacts(words)
    # joinFacts(factList)
    graph = makeGraph(facts)
    return

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

def makeGraph(facts):
    graph = Graph()
    for fact in facts:
        for x in fact:
            if x not in graph.keys():
                graph.addNode(x)


class Graph():
    def __init__(self):
        self.nodes = {}

    def addNode(self, letter):
        self.nodes[letter] = Node(letter)

    def keys(self):
        return self.nodes.keys()

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.edges  = []

    def addEdge(self, letter):
        edges.append(letter)

# words = []
# for x in xrange(50):
#     words.append('a' + chr(ord('a') + x) * 49)
# print timeit.timeit(lambda: makeFacts(words), number=1)
# facts = makeFacts(words)
# print timeit.timeit(lambda: joinFacts(facts), number=1)