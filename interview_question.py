# Merging sort ##O(n*log(n))##
def bubbleSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lethal = alist[:mid]
        rightful = alist[mid:]

        bubbleSort(lethal)
        bubbleSort(rightful)

        i = 0
        j = 0
        k = 0
        while i < len(lethal) and j < len(rightful):
            if lethal[i] < rightful[j]:
                alist[k] = lethal[i]
                i = i + 1
            else:
                alist[k] = rightful[j]
                j = j + 1
            k = k + 1

        while i < len(lethal):
            alist[k] = lethal[i]
            i = i + 1
            k = k + 1

        while j < len(rightful):
            alist[k] = rightful[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)
###2###BubbleSort
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
# for both:
mylist = [54, 26, 93, 17, 77, 23,-5,78,31, 44, 55, 20]
bubbleSort(mylist)
print(mylist)

# O(n) - matrix if it magic-square sum(row)= sum(Leftdiagonal)= sum(Leftdiagonal) = sum(colum)
def m(matrix):
    vSum = 0
    hSum = 0
    l1Sum = 0
    l2Sum = 0
    for i, v in enumerate(matrix):
        vSum += matrix[i][0]
        hSum += matrix[0][i]
        l1Sum += matrix[i][i]
        l2Sum += matrix[i][len(matrix) - i - 1]

    if vSum == hSum and vSum == l1Sum and vSum == l2Sum:
        return True
    return False
# matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1]]
# #matrix = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 1, 1, 1]]
# print(m(matrix))
# 4 - function get and sorted list and number,checks if there are 2 elements
# in the list whose sum is equal to the number.
# Without repeating an element twice   # O(2n)
def f(sorted_arr, sum):
    sec_nums = {}
    for num in sorted_arr:
        if not sec_nums.get(sum - num):
            sec_nums[sum - num] = 1
        else:
            sec_nums[sum - num] = +1
    for sec_num in sorted_arr:
        sec_exists = sec_nums.get(sec_num)
        if sec_num == sum - sec_num and sec_exists and sec_exists > 1:
            print(sec_num)
            return True
        if sec_num != sum - sec_num and sec_exists:
            print(sec_num)
            return True
    return False


arr = [2, 2, 4, 6, -2]
n = 6
print(f(arr, n))

#########Maxsanit_test##BinaryTreeSorting######
import random


# A Binary Tree Node 
class Node: 
  # Constructor to create a new node 
  def __init__(self, key): 
    self.key = key  
    self.left = None
    self.right = None
  

# A Binary Search Tree (BST)
class BinaryTree:
  root = None

  def inorder(self): 
    if self.root is not None: 
      BinaryTree.inorder_node(self.root) 
   
  def insert(self, key):
    if self.root is not None:
      BinaryTree.insert_node(self.root, key)
    else:
      self.root = Node(key)

  def max_value(self):
    if self.root is not None:
      node = BinaryTree.max_value_node(self.root)
      return node.key
    return None

  def delete(self, key):
    if self.root is not None:
      self.root = BinaryTree.delete_node(self.root, key)
      return key
    return None

  # A utility function to do inorder traversal of BST 
  @staticmethod
  def inorder_node(node): 
    if node is not None: 
      BinaryTree.inorder_node(node.left) 
      print(node.key) 
      BinaryTree.inorder_node(node.right) 
    
    
  # A utility function to insert a new node with given key in BST 
  @staticmethod
  def insert_node(node, key): 
    # If the tree is empty, return a new node 
    if node is None: 
      return Node(key) 
    # Otherwise recur down the tree 
    if key < node.key: 
      node.left = BinaryTree.insert_node(node.left, key) 
    else: 
      node.right = BinaryTree.insert_node(node.right, key) 
    # return the (unchanged) node pointer 
    return node 
    
  # Given a non-empty binary search tree, return the node 
  # with minum key value found in that tree. Note that the 
  # entire tree does not need to be searched 
  @staticmethod 
  def min_value_node(node): 
    current = node 
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
      current = current.left  
    return current  
    
  # Given a non-empty binary search tree, return the node 
  # with maximum key value found in that tree. Note that the 
  # entire tree does not need to be searched  
  @staticmethod
  def max_value_node(node): 
    current = node 
    # loop up to find the rightmost leaf 
    while(current.right is not None): 
      current = current.right  
    return current 

  # Given a binary search tree and a key, this function 
  # delete the key and returns the new root 
  @staticmethod
  def delete_node(root, key): 
    # Base Case 
    if root is None: 
      return root  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.key: 
      root.left = BinaryTree.delete_node(root.left, key) 
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.key): 
      root.right = BinaryTree.delete_node(root.right, key) 
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else:    
      # Node with only one child or no child 
      if root.left is None : 
        temp = root.right  
        root = None 
        return temp     
      elif root.right is None : 
        temp = root.left  
        root = None
        return temp 
      # Node with two children: Get the inorder successor 
      # (smallest in the right subtree) 
      temp = BinaryTree.min_value_node(root.right) 
      # Copy the inorder successor's content to this node 
      root.key = temp.key 
      # Delete the inorder successor 
      root.right = BinaryTree.delete_node(root.right , temp.key) 
    return root 


class OrderBox(object):
  box = BinaryTree()
  ref_arr = []

  def print(self):
    print('len:', len(self.ref_arr), ', values:')
    self.box.inorder()

  def push(self, number):
    self.box.insert(number)
    self.ref_arr.append(number)

  def pop(self):
    if len(self.ref_arr)>0:
      i = random.randrange(0, len(self.ref_arr))
      key = self.box.delete(self.ref_arr[i])
      del self.ref_arr[i]
      return key
    return None

  def max_value(self):
    return self.box.max_value()


box = OrderBox()
box.push(1)
box.push(4)
box.push(3)
box.push(4)
box.push(7)
box.push(9)

box.print()
print('pop:', box.pop())
print('max:', box.max_value())
print('pop:', box.pop())
print('max:', box.max_value())
print('pop:', box.pop())
print('max:', box.max_value())
#########################################
