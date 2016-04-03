def answer(numbers):
    visitedNodes = list()

    nextNode = numbers[0]
    visitedNodes.append(nextNode)
    while True:
        nextNode = numbers[visitedNodes[-1]]
        print "visiting " + str(nextNode)

        if nextNode in visitedNodes:
            return len(visitedNodes) - visitedNodes.index(nextNode)
        visitedNodes.append(nextNode)


print answer([1,0]) # should be 2
print answer([1,2,1]) # should be 2
print answer([1,3,0,1]) #should be 2
print answer([1,2,3,4,5,0]) #should be 6
