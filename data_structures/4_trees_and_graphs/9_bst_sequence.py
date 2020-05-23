from itertools import permutations
from binary_search_tree import Node, in_order_traversal

def gen_list(array, children):
    child_perms = []
    for permutation in permutations(children):
        temp = []
        for perm in permutation:
            temp.append(perm.data)
        child_perms.append(temp)
    l = []

    for perm in child_perms:
        for sub_array in array:
            l.append(sub_array + perm)
    return l

def bst_sequence(tree):
    parents = [tree]
    array = [[tree.data]]

    while parents:
        children = []

        for parent in parents:

            if parent.left:
                children.append(parent.left)

            if parent.right:
                children.append(parent.right)

        array = gen_list(array, children)
        parents = children
    return array


t = [8, 4, 10, 3, 6]
tree = Node(t[0])
for branch in t[1:]:
    tree.insert(branch)

print(bst_sequence(tree))

