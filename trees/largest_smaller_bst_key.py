

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node 
class Node:
# hello? Hello. Can you hear me?
# can't hear, just a min...
# OK
# can't hear or see, mind if I open a zoom room?
# er can you hear me?
# Sure. I can hear you by the way. Might be. from my end?
# Is this your first Pramp?

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    pass  # your code goes here
    # 1. Traverse the tree by checking right element
    # 2. If right element is bigger than input, go left
    # 3. If right is smaller than input, go right
    # 4. Edge cases
    
    # says connecting...
    # want to go zoom?
    node = self.root
    
    largest_smaller_key = float('inf')
    
    while(node is not None):
      # 2.      
      if(node.key < num):
        largest_smaller_key = node.key
        node = node.right          
      # 3.
      else:
        node = node.left
    
    return largest_smaller_key
  #First, make sure your peer understands the question.
# If you or your peer have a hard time understanding how to go about solving this problem, or could use a reminder of how BSTs work, take this interactive BST application for a spin.
# Some tend to first look for num in the tree and then look for its predecessor.
# However, num isn’t necessarily a key in the given tree. It could be any number. Moreover, even if num is in the tree, finding it first won’t help.
# To get the full score for problem solving, your peer must be able to explain why it’s possible to always store the last key smaller than num without comparing it to the previously stored key.

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11) 
bst.insert(14)   

result = bst.find_largest_smaller_key(17)

bst2 = BinarySearchTree()

# Hello. Trying to connect
# Are you able to see this text?
# yes
# let me open a zoom
# Yeah, try that. I can't see or hear anything now. Like you were before I think. Can you hear me at all though?
# https://usc.zoom.us/j/96640169654?pwd=bDNMY0l2Z2xCVEhrYUswbmhYL3p0QT09
# yea it's not the most reliable video chat if I recall...
# arg...
# can't hear anything
# I can hear you, but you sound like an alien
# man...must be me, one last try, have another zoom account...
# Let me try to change wifi. Pramp is telling me I have a connection problem
print ("Largest smaller number is %d " %(bst.find_largest_smaller_key(17)))
#
# lost you