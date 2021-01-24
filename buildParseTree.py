from stack import Stack
from BinaryTree import BinaryTree

## function to build a parse tree
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