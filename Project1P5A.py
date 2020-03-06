import random

#--------------------------- START BST RECURSIVE ---------------------------
class Node:
  def __init__(self,value):
    self.value = value
    self.parent = None
    self.left = None
    self.right = None
    self.height = 0
#Algorithms:
  #For Insert:
    #Check if root is null, if it is then tree is empty, making node the root of the tree.
    #If it isn't null, compare node to root, if greater than root, recursively call function to right of root, if less than, recursively call to the left of root
  #For FindMin:
    #All we do is go visit the left child of each subtree recursively.
    #Once the left child is null, we return the value of the node whose left child is null
  #For FindMax:
    #All we do is go visit the right child of each subtree recursively
    #Once the right child is null, we return the value of the node whose right child is null

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
  if root == None:
    return
  if root.value == value:
    if root.left != None:
      return findMaxRec(root.left)
  elif value < root.value:
    prevNode = root
    return findNextRec(root.left, prevNode, value)
  else:
    return findNextRec(root.right, prevNode, value)
#--------------------------- END BST RECURSIVE ---------------------------

#--------------------------- START AVL ---------------------------
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
    return findMaxIter(root.right)
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
  rebalance(parent)
 #--------------------------- END AVL ---------------------------
 #--------------------------- START GETRANDOM  ---------------------------
def getRandomArray(n):
  a = random.sample(range(1, n+1), n)
  return a

if __name__ == '__main__':
  BSTRoot = None
  AVLRoot = None
  randArray = getRandomArray(10000)
  for i in range(len(randArray)):
    AVLRoot = insertIter(AVLRoot, randArray[i])
    BSTRoot = insertIter(BSTRoot, randArray[i])

  
  
