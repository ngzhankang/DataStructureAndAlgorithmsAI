# declare space between nodes
COUNT = [7] 

# prints out the expression binary tree diagram level by level
class newNode: 
	# construct a new node 
	def __init__(self, key): 
		self.data = key 
		self.leftTree = None
		self.rightTree = None

# function to print binary tree in 2D
def print2DUtil(root, space) : 
	# base case if there is no root
	if (root == None) : 
		return

	# increases distance between levels 
	space += COUNT[0] 

	# process right child first 
	print2DUtil(root.rightTree, space) 

	# print current node after space count 
	print() 
	for i in range(COUNT[0], space): 
		print(end = " ") 
	print(root.key) 

	# process left child next
	print2DUtil(root.leftTree, space) 

# wrapper over print2DUtil() 
def print2D(root): 
	# pass initial space count as 0 
	print2DUtil(root, 0) 