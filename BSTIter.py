#Create a Node class
class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value

class BST:
  def __init__(self, root):
    self.root = root
  
  def insertIter(self, root, value):
    node = Node(value)
    #Starting with the root which is the current node in the tree
    curr = self.root
    #Parent will be following 'curr', basically the node on the level above curr
    parent = None

    #Jumping from node to node in the tree, either left or right depending if the value of the node is greater than or less than the current value. If greater, then jump to the right child, otherwise jump to the left.
    while curr != None:
      #Parent jumps to current node, making 'curr' the new parent node
      parent = curr
      if node.value > curr.value:
        #Jump right
        curr = curr.right
      else:
        #Jump left
        curr = curr.left
    #Checking if the tree is empty, if it is then the node becomes the parent 
    if parent == None:
      parent = node
    #If parent value > node value, then node gets assigned to parent and becomes left child
    elif parent.value > node.value:
      parent.left = node
    #If parent value < node value, then node gets assigned to parent and becomes right child
    else:
      parent.right = node
    return parent

  #Traversing down the left child of each left subtree until we hit a null
  def findMinIter(self, root):
    curr = self.root
    while curr.left != None:
      curr = curr.left
    return curr

  #Traversing down the right child of each right subtree until we hit a null
  def findMaxIter(self, root):
    curr = self.root
    while curr.right != None:
      curr = curr.right
    return curr
