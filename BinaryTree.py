class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
        
    # stores an object in root node
    def setKey(self, key):
        self.key = key
        
    # returns object stored in root node
    def getKey(self):
        return self.key
    
    # returns binary tree stored as child at left hand side
    def getLeftTree(self):
        return self.leftTree
    
    # returns binary tree stored as child at right hand side
    def getRightTree(self):
        return self.rightTree
    
    # creates a new binary tree and inserts it as child at left hand side
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
            
    # creates a new binary tree and inserts it as child at right hand side
    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree
            
    # print the expression tree in a pre-order manner
    def printPreorder(self, level):
        print( str(level*'#') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)