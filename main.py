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

def read_level(root, values, level, target):
  cost_tree_aux(root.left, values, level+1, lambda a, b, c: read_level(a,b,c,target))
  cost_tree_aux(root.right, values, level+1, lambda a, b, c: read_level(a,b,c,target))
  if level == target:
    values.append(root.value)

def cost_tree_aux(root, values, level, operation):
  if root == None:
    return
  else:
    operation(root, values, level)
    return

def cost_tree(root, operation):
  values = []
  cost_tree_aux(root, values, 0, operation)
  return values

#print(cost_tree(root, in_order))

def rep_tree(root, levels):
  for i in range(levels):
    #print(cost_tree(root, lambda a, b, c: read_level(a,b,c,i)))
    paint_level(cost_tree(root, lambda a, b, c: read_level(a,b,c,i)), i, levels)

def paint_level(row, level, levels):
  for num in range(pow(2, level)):
    if num == 0:
      insert_spaces(pow(2,levels - level) - 1)
      print("{:02d}".format(row[0]), end="")
      insert_spaces(pow(2,levels - level) - 1)
    else:
      insert_spaces(pow(2, levels - level))
      print("{:02d}".format(row[num]), end="")
      insert_spaces(pow(2, levels - level) - 1)
  print("")

def insert_spaces(num):
  for i in range(num):
    print("--", end="")

#rep_tree(root, 4)

def accumulate_tree(root, add):
  if root == None:
    return None
  else:
    return Tree(accumulate_tree(root.left, root.value + add), accumulate_tree(root.right, root.value + add), root.value + add)

rep_tree(accumulate_tree(root, 0), 4)

def minimax(root, level):
  if (root.left == None) and (root.right == None):
    return root.value
  else:
    left = minimax(root.left, level + 1)
    right = minimax(root.right, level + 1)
    if level % 2 == 0:
      return left if (left > right) else right
    else:
      return left if (left < right) else right

test15 = Tree(None, None, -1)
test14 = Tree(None, None, 0)
test13 = Tree(None, None, 2)
test12 = Tree(None, None, 1)
test11 = Tree(None, None, 9)
test10 = Tree(None, None, 6)
test9 = Tree(None, None, 5)
test8 = Tree(None, None, 3)
test7 = Tree(test14, test15, 10)
test6 = Tree(test12, test13, 10)
test5 = Tree(test10, test11, 10)
test4 = Tree(test8, test9, 10)
test3 = Tree(test6, test7, 10)
test2 = Tree(test4, test5, 10)
test1 = Tree(test2, test3, 10)

print(minimax(test1, 0))

def alphabeta(root, level, alpha, beta):
  if (root.left == None) and (root.right == None):
    return root.value
  else:
    left = minimax(root.left, level + 1,)
    right = minimax(root.right, level + 1,)
    if level % 2 == 0:
      return left if (left > right) else right
    else:
      return left if (left < right) else right

print(alphabeta(test1, 0, -10000, 10000))