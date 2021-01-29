import os.path
from BinaryTree import BinaryTree
from Expression import Expression
from node import Node
from sortedList import sortedList
from stack import Stack
from HashTable import HashTable
from Equations import Equations
from treeLayout import treeLayout

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

    choice = ''
    
    # loop to run the selection menu
    while choice != '3':
        choice = input('Enter Choice: ')
        if choice == '1':
            choice1()
        if choice == '2':
            choice2()
        if choice == '3':
            choice3()
        else:
            print("Invalid input! Please input 1, 2 or 3!")
            
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
        # concatenate negative symbol to number
        elif exp[x] == '-' and exp[x-1] in ['+', '-', '*', '/', '**', '(']:
            no += exp[x]
        # concatenate asterik to another asterik
        elif (exp[x] == "*" and exp[x-1] == "*"):
            del tokens[-1]
            ast = '**'
            tokens.append(ast)
            ast = ""
        # concatenate slash to another slash
        elif (exp[x] == "/" and exp[x-1] == "/"):
            del tokens[-1]
            ast = "//"
            tokens.append(ast)
            ast = ""
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
        elif t in ['+', '-', '*', '/', '**', '//', '%']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree() 
        # RULE 3: If token is number, set key of the current node to that number and return to parent
        elif t not in ['+', '-', '*', '/', '**', '//', '%', ')'] :
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
        elif op == '//':
            return float(evaluate(leftTree)) // float(evaluate(rightTree))
        elif op == "%":
            return float(evaluate(leftTree)) % float(evaluate(rightTree))
    else:
        return tree.getKey()

# function to sort the equations by length
def mergeSort(l):
    if len(l) > 1:
        mid = int (len(l)/2) # Split the length of list into 2 to speed up
        leftHalf = l[:mid] # Left side of the list
        rightHalf = l[mid:] # Right side of list
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        # Decalare the starting indexes as 0
        leftIndex,rightIndex,mergeIndex = 0,0,0
        
        # Declare mergeList as l (list)
        mergeList = l
          
        # Handle those items still left in both the left half and right half
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
            mergeIndex+=1

        # Handle those items still left in the left Half
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex+=1
            mergeIndex+=1
            
        # Handle those items still left in the right Half
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex+=1
            mergeIndex+=1

# main functions
# function to carry out choice 1  
def choice1():
    exp = input("Please enter the expression you want to evaluate: \n")
    print()
    tree = buildParseTree(exp)
    print("How do you want to print the parse tree?")
    print("  1. Pre-order")
    print("  2. Post-order")
    print("  3. In-order")
    print("  4. Exit")
    printSelect = ''
    while printSelect != '4':
        printSelect = input(">>> ")
        print()
        if printSelect == '1':
            print("Expression Tree: ")
            tree.printPreorder(0)
            print()
            # tl = treeLayout(tree)
            # for n in (BinaryTree):
            #     tl.insert(BinaryTree)
            # tl.display()
            print(f'Expression evaluates to: \n{evaluate(tree)} \n')  
            input("Press any key, to continue....")
            selectionMenu()
        if printSelect == '2':
            print("Expression Tree: ")
            tree.printPostorder(0)
            print()
            print(f'Expression evaluates to: \n{evaluate(tree)} \n')  
            input("Press any key, to continue....")
            selectionMenu()
        if printSelect == '3':
            print("Expression Tree: ")
            tree.printInorder(0)
            print()
            print(f'Expression evaluates to: \n{evaluate(tree)} \n')  
            input("Press any key, to continue....")
            selectionMenu()
        if printSelect == '4':
            choice3()
        else:
            print("Invalid input! Please input 1, 2, 3 or 4!")

# function to carry out choice 2
def choice2():
    # create a compare list to append the corrected list
    unstructured_list = []
    eqn_list = []
    print()
    inputFile = input("Please enter input file: ")
    while True:
        if os.path.isfile(inputFile): break
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
        tree = buildParseTree(expressions)

        # here we evaluate the expression and then sort by value
        eqn_list.append(expressions)
        l.insert(Expression(evaluate(tree)))
        unstructured_list.append(Expression(evaluate(tree)))
    f.close()

    # make a dictionary for the eqn and the values
    dictionary = dict(zip(eqn_list, unstructured_list))

    # change the positions of key and value in the dictionary arranged from smallest val to largest val
    def order(x, y):
        if x[1] < y[1]: return x, y
        else: return y, x
            
    # do a bubble sort
    def bubble(mydict):
        d_items = list(mydict.items())
        for j in range(len(d_items) - 1):
            for i in range(len(d_items) - 1):
                d_items[i], d_items[i+1] = order(d_items[i], d_items[i+1])
        return d_items
        
    sorted_tuples = bubble(dictionary)
    new_list = []
    for n in sorted_tuples:
        if len(new_list) == 0: new_list.append([n])
        else:
            if new_list[-1][-1][1] == n[1]:
                new_list[-1].append(n)
            else: new_list.append([n])
    print(new_list)
    print()
    
    # sort the lists according to length of expressions
    def sortLength(tup):
        lst = len(tup)
        for i in range(0, lst):
            for x in range(0, i):
                for j in range(0, lst-x-1):
                    if (len(tup[j][0]) > len(tup[j+1][0])):
                        temp = tup[j]
                        tup[j] = tup[j+1]
                        tup[j+1] = temp
        return tup

    print(sortLength(new_list))
    



    # append into the HashTable
    # size = len(eqn_list)
    # eqnTable = HashTable(size)



    # for i in range(size):
    #     eqnTable[i] = 
    # HashTable.sorting(eqn_list, unstructured_list, structured_list)


    # write sorted expressions into output file
    # f = open(outputFile, 'w')
    # Expression = l.resetForIteration()
    # while Expression != None:
    #     f.write(float(str(Expression.name+"\n")))
    #     Expression = l.nextNode()
    # f.close()

    
    print(">>>Evaluation and sorting completed!")
    input("Press any key, to continue....")
    selectionMenu()

# function to carry out choice 3
def choice3():
    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
    exit()

selectionMenu()