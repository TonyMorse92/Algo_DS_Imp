# Basic binary tree

class Tree:
	def __init__(self, node):
		self.node = node
		self.left_child = None
		self.right_child = None



# Test

root = Tree("root")
root.left_child = Tree("left")
root.right_child = Tree("right")
root.right_child.right_child = Tree("rightyright")


print(root)
