class sortedList:
    # constructor
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0
    # append the next node as the head node
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    # insert new node
    def insert(self, newNode):
        self.length += 1
        # if list is empty
        if self.headNode == None:
            self.headNode = newNode
            return
        # check if new node is going to be the new head node
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return
        # check if new node is going to be inserted between any pair of nodes (left,right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # if does not meet any criteria above, add to tail
        leftNode.nextNode = newNode

    # create the output format
    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (',' + node.__str__())
            node= node.nextNode
        return output
    
    # reset for each iteration
    def resetForIteration(self):
        self.currentNode = self.headNode
        return self.currentNode

    # call the current node as the next node so that all nodes will be checked
    def nextNode(self):
        self.currentNode = self.currentNode.nextNode
        return self.currentNode