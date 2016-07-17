from collections import OrderedDict, deque
import timeit
from itertools import islice, izip

def answer(words):
    facts = makeFacts(words)
    graph = makeGraph(facts)
    return topologicalSort(graph)

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
            if len(words[i]) > 1:
                wordsToMakeMoreFactsFrom = [words[i][1:]]
            continue
        else:
            if len(words[i]) > 1:
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
        for x in izip(fact, fact[1:]):
            if x[0] not in graph.keys():
                graph.addNode(x[0])
            if x[1] not in graph.keys():
                graph.addNode(x[1])
            graph.nodes[x[0]].addEdge(x[1])
    return graph

def topologicalSort(graph):
    sortedNodes  = deque()
    visitedNodes = []
    markedNodes  = []

    def visit(node):
        if node in markedNodes:
            raise Exception("Not a directed acyclic graph")
        elif node not in visitedNodes:
            markedNodes.append(node)
            for edge in node.edges:
                visit(graph.nodes[edge])
            visitedNodes.append(node)
            markedNodes.remove(node)
            sortedNodes.appendleft(node.letter)

    for node in graph.values():
        if node not in visitedNodes:
            visit(node)

    return ''.join(sortedNodes)

class Graph():
    def __init__(self):
        self.nodes = {}

    def addNode(self, letter):
        self.nodes[letter] = Node(letter)

    def keys(self):
        return self.nodes.keys()

    def values(self):
        return self.nodes.values()

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.edges  = []

    def addEdge(self, letter):
        if letter not in self.edges:
            self.edges.append(letter)

# words = []
# for x in xrange(50):
#     words.append('a' + chr(ord('a') + x) * 49)
# print timeit.timeit(lambda: makeFacts(words), number=1)
# facts = makeFacts(words)
# print timeit.timeit(lambda: joinFacts(facts), number=1)