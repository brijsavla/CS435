class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
#First we recurse down the left tree, then we recurse down the right tree
def inOrder(root):
  inOrder(root.left)
  inOrder(root.value)
  inOrder(root.right)

