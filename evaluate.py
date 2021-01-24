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