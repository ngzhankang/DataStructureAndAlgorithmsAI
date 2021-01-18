######  The classes must be placed in separate python files  ######

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
        if Choice == '3':
            choice3()
        else:
            print("Invalid input! Please input 1, 2 or 3!")

# stack class 
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
        print( str(level*'-') + str(self.key))
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
    tempKey = input("Press any key, to continue....")
    selectionMenu()

# function to carry out choice 3
def choice3():
    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
    exit()

selectionMenu()