#Create a Node class
class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value

def insertRec(root, node):
  #Check if root is null, if it is then tree is empty, making node the root of the tree.
  if root is None:
    root = node
  #If it isn't null, compare node to root, if greater than root, recursively call function to right of root, if less than, recursively call to the left of root
  else:
    #Right child
    if root.value < node.value:
      #Checking to see if there is a right child, if not then node is the right child
      if root.right is None:
        root.right = node
      #Recursively call insert on the right child
      else:
        insertRec(root.right, node)
    #Left child
    else:
      #Same as above but this time on the left
      if root.value > node.value:
        if root.left is None:
          root.left = node
        else:
          insertRec(root.left, node)

def findMinRec(node):
  #Once the left child of the node is null, we return the node
  if node.left == None:
    return node
  #Call findMin recursively until node with left child is null.
  return findMinRec(node.left)

def findMaxRec(node):
  #Once the right child of the node is null, we return the node
  if node.right == None:
    return node
  #Call findMax recursively until node with right child is null.
  return findMaxRec(node.right)

#Finding the next node in the tree
def findNextRec(root, nextNode, value):
  #Base case, if null, return null
  if root == None:
    return
  #If we find the root value in the tree, find the minimum of the right child of root.
  if root.value == value:
    #Checks to see if there is a right value for root
    if root.right != None:
      return findMinRec(root.right)
  #If value is less than the root value, the next node becomes root, then recursively call on the left child of root.
  elif value < root.value:
    nextNode = root
    return findNextRec(root.left, nextNode, value)
  else:
    return findNextRec(root.right, nextNode, value)

#Finding the previous node in the tree, basically opposite of findNextRev
def findPrevRec(root, prevNode, value):
  if root is None:
    return
  if root.value == value:
    if root.left != None:
      return findMaxRec(root.left)
  elif value < root.value:
    nextNode = root
    return findNextRec(root.left, prevNode, value)
  else:
    return findNextRec(root.right, prevNode, value)
