from collections import deque
from itertools import izip

def answer(words):

    graph = makeGraphFromWords(words)
    return topologicalSort(graph)

def makeGraphFromWords(words):
    graph = Graph()
    for x in xrange (len(words) - 1):
        firstWord = words[x]
        secondWord = words[x+1]
        maxLength = max(len(firstWord), len(secondWord))
        for letterPair in zip(firstWord[:maxLength], secondWord[:maxLength]):
            graph.addNode(letterPair[0])
            graph.addNode(letterPair[1])
            if letterPair[0] == letterPair[1]:
                continue
            else:
                graph.nodes[letterPair[0]].addEdge(letterPair[1])
                break
    return graph

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
        if letter not in self.keys():
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
