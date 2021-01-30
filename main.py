# import necessary classes
import os.path
from BinaryTree import BinaryTree
from Expression import Expression
from Expression2 import Expression2
from node import Node
from sortedList import sortedList
from Stack import Stack
from treeLayout import treeLayout

# print the selection menu
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
            
# build a parse tree
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

# evaluate the expression
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

# sorting using merge sort method
def mergeSort(l):
    for i in l:
        if len(l) > 1:
            mid = int (len(l)/2) 
            leftHalf = l[:mid]
            rightHalf = l[mid:] 
            mergeSort(leftHalf)
            mergeSort(rightHalf)
            
            # declare the starting indexes as 0
            leftIndex,rightIndex,mergeIndex = 0,0,0
            
            # declare mergeList as l (list)
            mergeList = l
            
            # handle those items still left in both the left half and right half
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
                mergeIndex+=1

            # handle those items still left in the left Half
            while leftIndex < len(leftHalf):
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
                mergeIndex+=1
                
            # handle those items still left in the right Half
            while rightIndex < len(rightHalf):
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
                mergeIndex+=1

# change the positions of key and value in the dictionary arranged from smallest val to largest val
def order(x, y):
    if x[1] < y[1]: 
        return x, y
    else: 
        return y, x
        
# do a bubble sort to sort by value
def bubble(mydict):
    d_items = list(mydict.items())
    for j in range(len(d_items) - 1):
        for i in range(len(d_items) - 1):
            d_items[i], d_items[i+1] = order(d_items[i], d_items[i+1])
    return d_items

# sort by equation length
def sortLength(lists):
    # this is the index to determine location in the big list
    index = 0 
    for x in lists:
        # if it is a single element list
        if len(x) == 1:
            index += 1
            continue
        else:
            eqn_list = []
            # if it is a multiple element lists
            for n in x: # loop through the big list
                eqn_list.append(Expression2(n[0]))

            mergeSort(eqn_list)
            temp_list = []

            for i in range(0, len(eqn_list), 1):
                temp_tuple = list(x[i])
                temp_tuple[0] = eqn_list[i]
                back_tuple = tuple(temp_tuple)
                temp_list.append(back_tuple)

            lists[index] = temp_list
            index += 1
    return lists

# encapsulate each item in the list with [] to allow for comparison with another list
def extractDigits(lst): 
    res = [] 
    for el in lst: 
        sub = el.split(', ') 
        res.append(sub) 
    return(res) 

# main functions
# function to carry out choice 1  
def choice1():
    exp = input("Please enter the expression you want to evaluate: \n")
    tree = buildParseTree(exp)
    print()
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
        if os.path.isfile(inputFile): 
            break
        else:
            print('Invalid file name! File not found!')
            inputFile = input("Please enter valid input file: ")        
    outputFile = input("please enter output file: ")
    print()
    print(">>>Evaluation and sorting started:")
    print()
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

    # make a dictionary for the equation and values
    dictionary = dict(zip(eqn_list, unstructured_list))

    # bubble sort the dictionary
    sorted_tuples = bubble(dictionary)
    new_list = []

    # loop through the tuples in the list and encapsulate tuples with similar values together with []
    for n in sorted_tuples:
        if len(new_list) == 0: 
            new_list.append([n])
        else:
            if new_list[-1][-1][1] == n[1]:
                new_list[-1].append(n)
            else: 
                new_list.append([n])
    
    # sort the list that is sorted by value based on length of equation
    finalSorted = sortLength(new_list)
    
    temp_valList = [[x[1] for x in l] for l in finalSorted]
    expList = [[x[0] for x in l] for l in finalSorted]
    valList = []
    valsList = []

    # remove duplicate values
    for i in temp_valList:
        for x in i:
            if x not in valList:
                valList.append(x)
    
    # get rid of quotes from values
    for g in valList:
        value = str(g).strip('"\'')
        valsList.append(value)

    # get the list back with each item encapsulated by []
    valList = extractDigits(valsList)   
    
    # zip valList and expList so that we can compare the 2 list
    # then we print based on list index
    for val, exp in zip(valList, expList):
        result = val[0]
        print(f'*** Expressions with value = {result}')
        for e in exp:
            print(f'{e} ==> {result}')
        print()
        
    # write sorted expressions into output file
    f = open(outputFile, 'w')
    for val, exp in zip(valList, expList):
        result = val[0]
        f.write(f'*** Expressions with value = {result}\n')
        for e in exp:
            f.write(f'{e} ==> {result}\n')
        f.write('\n')
    f.close()

    print(">>>Evaluation and sorting completed!")
    input("Press any key, to continue....")
    selectionMenu()

# function to carry out choice 3
def choice3():
    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter")
    exit()

selectionMenu()