class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.left = None
    self.right = None
    self.height = 0
#Gets height of current node
def getHeight(curr):
  if curr != None:
    return curr.height
  else:
    return -1
#Updates the height of current node
def updateHeight(curr):
  if curr != None:
    curr.height = max(getHeight(curr.left), getHeight(curr.right)) + 1
#Determining the balance factor
def calcBF(curr):
  leftHeight = getHeight(curr.left)
  rightHeight = getHeight(curr.right)
  bf = leftHeight-rightHeight
  return bf
#This is the function to rotate left
#Every time we do a rotation, we are going to update the heights
def leftRotate(curr):
  temp = curr.right
  curr.right = temp.left
  temp.left = curr
  updateHeight(curr)
  updateHeight(temp)
  return temp
#This is the function to rotate right
def rightRotate(curr):
  temp = curr.left
  curr.left = temp.right
  temp.right = curr
  updateHeight(curr)
  updateHeight(temp)
  return temp
#Function that will determine if tree is balanced after insertion or deletion
def isBalanced(curr):
  if curr == None:
    return True
  else:
    return abs(calcBF(curr)) <= 1
#This rebalances the tree after insertion or deletion if the tree is left heavy or right heavy
def rebalance(root):
  bf = calcBF(root)
  #Checking the left heavy cases
  if bf > 1:
    leftBF = calcBF(root.left)
    #To check if it is a left right case
    if leftBF < 0:
      root.left = leftRotate(root.left)
    #If above if statement doesn't execute, then it's a left-left heavy tree
    root = rightRotate(root)
    return root
  #Right heavy cases
  else:
    rightBF = calcBF(root.right)
    #Checking if it's right left case 
    if rightBF > 0:
      root.right = rightRotate(root.right)
    #Otherwise it is a right-right case
    root = leftRotate(root)
    return root
#Finding the max element in the tree
def findMaxIter(root):
  curr = root
  while curr.right != None:
    curr = curr.right
  return curr
#Finding the min element in the tree
def findMinIter(root):
  curr = root
  while curr.left != None:
    curr = curr.left
  return curr
#Finding the successor of a node
def findNextIter(root, value):
  if root.right != None:
    return findMinIter(root.right)
  curr = root.parent
  while curr != None:
    if curr.value > root.value:
      return curr
    curr = curr.parent
  return None
#Finding the successor of a node
def findPrevIter(root, value):
  if root.right != None:
    return findMaxIter(root.left)
  curr = root.parent
  while curr != None:
    if curr.value > root.value:
      return curr
    curr = curr.parent
  return None
#Insert a node into an AVL Tree
def insertIter(root, value):
  node = Node(value)
  curr = root
  parent = None
  #1. BST Insertion
  while curr != None:
    parent = curr
    if node.value > curr.value:
      curr = curr.right
    else:
      curr = curr.left
  if parent == None:
    parent = node
  elif parent.value > node.value:
    parent.left = node
  else:
    parent.right = node
  return parent
  #2. Update the height
  updateHeight(parent)
  #3. Rebalance tree if needed
  if not isBalanced(parent):
    rebalance(parent)
