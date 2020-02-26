
#Create a Node class
class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value
#Algorithms:
  #For Insert:
    #Check if root is null, if it is then tree is empty, making node the root of the tree.
    #If it isn't null, compare node to root, if greater than root, recursively call function to right of root, if less than, recursively call to the left of root
  #For Delete:
    #This function has 3 parts to the algorithm:
      #1. No children
        #Just remove the node from the tree
      #2. One child
        #Swap child with parent and delete parent
      #3. Two children
        #Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. 
        #Note that inorder predecessor can also be used.
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
