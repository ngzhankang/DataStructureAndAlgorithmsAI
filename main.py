import os.path
from BinaryTree import BinaryTree
from buildParseTree import buildParseTree
from evaluate import evaluate
from Expression import Expression
from node import Node
from sortedList import sortedList
from stack import Stack

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
    # create a compare list to append the corrected list
    compare_list = []

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
        print(Expression(evaluate(tree)))
        l.insert(Expression(evaluate(tree)))

        # append into an array for comparison
        if len(compare_list) == 0:
            compare_list.append(l)
        else:
            compare_list.remove(compare_list[0])
            compare_list.append(l)
        print(compare_list)
        print()
    f.close()

    # write sorted expressions into output file
    # f = open(outputFile, 'w')
    # expressions = l.resetForIteration()
    # while expressions != None:
    #     print(expressions, 'HERE')
    #     f.write(expressions.name+"\n")
    #     expressions = l.nextNode()
    # f.close()

    
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