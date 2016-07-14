import Queue

def answer(food, grid):
    # useAstar = False
    #
    # if useAstar:
    #     startAstar(food)
    # else:
    #     leftovers = startPQueueSearch(food, grid)
    #     #startBruteSearch(food)
    #
    # return leftovers
    leftovers = findSmallestLeftoverFoodForLocation(grid, food, len(grid) - 1, len(grid) -1)
    return leftovers if leftovers <= food else -1

def getAnswerFromList(leftovers):
    if len(leftovers) == 0:
        return -1
    else:
        return min(leftovers)


def startBruteSearch(food):
    openNodes = Queue.Queue()
    openNodes.put([food, [0,0]])

    while not openNodes.empty():
        try:
            item = openNodes.get(block=False)
            search(item[0], item[1])
        except:
            break

def search(foodLeft, location):
    global globalGrid
    global openNodes
    global leftoverList
    global gridSize

    x,y = location[0], location[1]

    foodLeft -= globalGrid[x][y]
    if foodLeft >= 0:
        if x < gridSize - 1:
            openNodes.put([foodLeft, [ x+1, y  ]])
        if y < gridSize - 1:
            openNodes.put([foodLeft, [ x  , y+1]])

        if x == gridSize - 1 and y == gridSize -1:
            leftoverList.append(foodLeft)

class LessThanNode:
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def __cmp__(self, other):
        return cmp(self.food, other.food)

class GreaterThanNode:
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def __cmp__(self, other):
        return self.food > other.food

def startPQueueSearch(food, grid):
    gridSize = len(grid)
    possibleAnswers = []

    openNodes = Queue.PriorityQueue()
    openNodes.put(LessThanNode(food, [0,0]))

    while not openNodes.empty():
        currentNode = openNodes.get()
        foodLeftAfterCurrent = currentNode.food - grid[currentNode.location[0]][currentNode.location[1]]

        if foodLeftAfterCurrent >= 0:
            if currentNode.location == [gridSize - 1, gridSize - 1]:
                possibleAnswers.append(foodLeftAfterCurrent)
            addNeighborsToQueue(currentNode, openNodes, gridSize, foodLeftAfterCurrent)

    return getAnswerFromList(possibleAnswers)

def addNeighborsToQueue(currentNode, openNodes, gridSize, foodLeft):
    neighbors = getNeighbors(currentNode, gridSize)
    for location in neighbors:
        openNodes.put(LessThanNode(foodLeft, location))

def startAstar(food):
    global gridSize
    openNodes = Queue.PriorityQueue() #maybe there's a faster structure?
    openNodes.put(Node(food, [0,0]))

    closedNodes = []

    while not openNodes.empty():
        currentNode = openNodes.get()

        if currentNode.location == [gridSize, gridSize]:
            return currentNode.food

        closedNodes.append(currentNode)

        neighbors = getNeighbors(currentNode.location, gridSize)
        for candidateNode in neighbors:
            if candidateNode in closedNodes: # need to check if this works?
                continue


def getNeighbors(node, gridSize):
    neighbors = []
    if node.location[0] < gridSize - 1:
        neighbors.append([node.location[0] + 1, node.location[1]])
    if node.location[1] < gridSize - 1:
        neighbors.append([node.location[0], node.location[1] + 1])

    return neighbors


def findSmallestLeftoverFoodForLocation(grid, foodLeft, i, j):
    if i < 0 or j < 0 or foodLeft < 0:
        return 201 # one more than maximum starting value
    elif i == j == 0:
        return foodLeft
    else:
        foodLeft -= grid[i][j]
        return min(findSmallestLeftoverFoodForLocation(grid, foodLeft, i - 1, j), findSmallestLeftoverFoodForLocation(grid, foodLeft, i, j - 1))