class Tree(object):
  def __init__(self, left, right, value):
    self.left = left
    self.right = right
    self.value = value

n15 = Tree(None, None, 10)
n14 = Tree(None, None, 9)
n13 = Tree(None, None, 7)
n12 = Tree(None, None, 6)
n11 = Tree(None, None, 5)
n10 = Tree(None, None, 1)
n9 = Tree(None, None, 8)
n8 = Tree(None, None, 4)
n7 = Tree(n14, n15, 3)
n6 = Tree(n12, n13, 2)
n5 = Tree(n10, n11, 6)
n4 = Tree(n8, n9, 7)
n3 = Tree(n6, n7, 4)
n2 = Tree(n4, n5, 3)
root = Tree(n2, n3, 1)

def in_order(root, values, level):
  cost_tree_aux(root.left, values, level+1, in_order)
  values.append(root.value)
  cost_tree_aux(root.right, values, level+1, in_order)

def pre_order(root, values, level):
  values.append(root.value)
  cost_tree_aux(root.left, values, level+1, pre_order)
  cost_tree_aux(root.right, values, level+1, pre_order)

def post_order(root, values, level):
  cost_tree_aux(root.left, values, level+1, post_order)
  cost_tree_aux(root.right, values, level+1, post_order)
  values.append(root.value)

def cost_tree_aux(root, values, level, operation):
  if root == None:
    return
  else:
    operation(root, values, level)
    return

def cost_tree(root):
  values = []
  cost_tree_aux(root, values, 0, in_order)
  print(values)

cost_tree(root)

