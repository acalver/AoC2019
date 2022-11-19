from anytree import Node
eg = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
tree_elements = set()

i = 0
test = eg[i].split(')')

if test[0] in tree_elements:
    globals()[test[1]] = Node(test[1], parent =  globals()[test[0]])

else:
    globals()[test[0]] = Node(test[1])

tree_elements = tree_elements.union(set(test))


i += 1
