######  The classes must be placed in separate python files  ######
import os.path

# function to print the selection menu
def selectionMenu():
    print('*' * 62)
    print('* ST1507 DSAA: Expression Evaluator & Sorter {:>17}'.format('*'))
    print('*' + '-' * 60 + '*')
    print('* {:>60}'.format('*'))
    print('*  ' + '- Done by: Ng Zhan Kang(1935727) & Triston Loh(1935488) {:>3}'.format('*'))
    print('*  ' + '- Class DIT/2B/11 {:>41}'.format('*'))
    print('*' * 62)
    print()
    print("Please select your choice ('1','2','3'):")
    print("  1. Evaluate expression")
    print("  2. Sort expressions")
    print("  3. Exit")

    Choice = ''
    
    # loop to run the selection menu
    while Choice != '3':
        Choice = input('Enter Choice: ')
        if Choice == '1':
            choice1()
        if Choice == '2':
            choice2()
        if Choice == '3':
            choice3()
        else:
            print("Invalid input! Please input 1, 2 or 3!")

class Stack:
    def __init__(self):
        self.__list= []
        
    # empty list
    def isEmpty(self):
        return self.__list == []
    
    # get size of list
    def size(self):
        return len(self.__list)
    
    # clear items of list
    def clear(self):
        self.__list.clear() 
    
    # push item into back of list
    def push(self, item):
        self.__list.append(item)
        
    # extract last item of list
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
        
    # get items of list
    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    
    # returns output in neat format
    def __str__(self):
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output

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

# function to build a parse tree
def buildParseTree(exp):
    # tokenize the expression
    tokens = []
    no = ""
    ast = ""
    for x in range(0, len(exp)):
        # skip spaces
        if exp[x] == " ":pass
        # concatenate digits or '.' to number
        elif exp[x].isdigit() or (exp[x] == "."):
            no += exp[x]
        # concatenate asterik to another asterik
        elif (exp[x] == "*" and exp[x-1] == "*"):
            del tokens[-1]
            ast = '**'
            tokens.append(ast)
            ast = ""
        # other token: append number if any, and then token
        else:
            if no != "":
                tokens.append(no)
            tokens.append(exp[x])
            no = ""
            
    stack = Stack()
    tree = BinaryTree('?')
    stack.push(tree)
    currentTree = tree
    
    for t in tokens:
        # RULE 1: If token is '(' add a new node as left child and descend into that node
        if t == '(':
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree()
        # RULE 2: If token is operator, set key of current node to that operator and add a new node as right child and descend into that node
        elif t in ['+', '-', '*', '/', '**']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree() 
        # RULE 3: If token is number, set key of the current node to that number and return to parent
        elif t not in ['+', '-', '*', '/', '**', ')'] :
            currentTree.setKey(t)
            parent = stack.pop()
            currentTree = parent
        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree

# function to evaluate the expression
def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()
    
    # loop to return the true value of each pair of terms of the expression
    if leftTree != None and rightTree != None:
        if op == '+':
            return float(evaluate(leftTree)) + float(evaluate(rightTree))
        elif op == '-':
            return float(evaluate(leftTree)) - float(evaluate(rightTree)) 
        elif op == '*':
            return float(evaluate(leftTree)) * float(evaluate(rightTree))
        elif op == '**':
            return float(evaluate(leftTree)) ** float(evaluate(rightTree))
        elif op == '/':
            return float(evaluate(leftTree)) / float(evaluate(rightTree))
    else:
        return tree.getKey()

class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None

class Expression(Node):
    def __init__(self, name):
        self.name = name
        super().__init__()
        
    def __str__(self):
        return f"'{self.name}'"
    
    def __eq__(self,otherNode):
        if otherNode == None:
            return False
        else:
            return self.name == otherNode.name
        
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Expression' and 'NoneType'")
        if len(self.name) == len(otherNode.name):
            return self.name[0] < otherNode.name[0]
        return len(self.name) < len(otherNode.name)

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


# main functions
# function to carry out choice 1  
def choice1():
    exp = input("Please enter the expression you want to evaluate: \n")
    print()
    print("Expression Tree: ")
    tree = buildParseTree(exp)
    tree.printPreorder(0)
    print()
    print(f'Expression evaluates to: \n{evaluate(tree)} \n')  
    input("Press any key, to continue....")
    selectionMenu()

def choice2():
    print()
    inputFile = input("Please enter input file: ")
    while True:
        if os.path.isfile(inputFile):
            break
        else:
            print('Invalid file name! File not found!')
            inputFile = input("Please enter valid input file: ")        
    outputFile = input("please enter output file: ")
    print()
    print(">>>Evaluation and sorting started")
    l = sortedList()
    # read expressions from input file and sort in list
    f = open(inputFile, 'r')
    for expressions in f:
        expressions = expressions.strip() 
        l.insert(Expression( expressions ))
    f.close()
    # write sorted expressions into output file
    f = open(outputFile, 'w')
    expressions = l.resetForIteration()
    while expressions != None:
        f.write(expressions.name+"\n")
        expressions = l.nextNode()
    f.close()
    f = open(outputFile, 'r')
    for exp in f:
        exp = exp.split()
        for elem in exp:
            # print(elem)
            tree = buildParseTree(elem)
            # tree.printPreorder(0)
            print(evaluate(tree))
    
    print(">>>Evaluation and sorting completed!")
    # tree = buildParseTree(l)
    # print(tree)
    input("Press any key, to continue....")
    selectionMenu()

# function to carry out choice 3
def choice3():
    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
    exit()

selectionMenu()