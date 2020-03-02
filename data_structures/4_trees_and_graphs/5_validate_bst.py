from binary_search_tree import Node
from binary_tree import Node as b_node

def is_bst(tree: object) -> bool:
    """
        checks if a  given binary tree is a binary search tree based on left_node < node < right_node
        WARNING: This algo doesn't checks if all nodes on left are lesser than the current node and
                 if  all nodes on right are greater than the current node
    """
    if tree:

        parents = [tree]

        while parents:
            children = []

            for parent in parents:
                
                # check left node
                if parent.left:
                    if parent.left.data > parent.data:
                        return False
                    else:
                        children.append(parent.left)
                
                # check right node
                if parent.right:
                    if parent.right.data < parent.data:
                        return False
                    else:
                        children.append(parent.right)
            parents = children
        
        return True

def is_correct_bst(tree):
    """
        Completely checks if all of left_nodes < node < all of right_nodes
    """
    return check_bst(tree, None, None)

def check_bst(node, min_, max_):
    """
        Recursively checks all nodes
    """
    if not node:
        return True
    
    if min_:
        if node.data <= min_:
            return False        
    
    if max_:
        if node.data > max_:
            return False
    
    if (not check_bst(node.left, min_, node.data)) or (not check_bst(node.right, node.data, max_)):
        return False
    
    return True



if __name__ == "__main__":
    tree = Node()
    values = [8, 4, 10, 2, 6, 20]
    for value in values:
        tree.insert(value)
    
    print(is_bst(tree))

    b_tree = b_node(12)
    b_tree.left = b_node(14)
    b_tree.right = b_node(16)
    b_tree.left.left = b_node(8)
    b_tree.left.right = b_node(15)
    b_tree.right.left = b_node(24)
    b_tree.right.right = b_node(20)
    print(is_bst(b_tree))
    
    bug = b_node(20)
    bug.left = b_node(10)
    bug.left.right = b_node(25)
    bug.right = b_node(30)
    print(is_bst(bug))
    print(is_correct_bst(bug))
    