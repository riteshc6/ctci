from binary_search_tree import Node
from binary_tree import Node as b_node

def is_bst(tree: object) -> bool:
    """
        checks if a  given binary tree is a binary search tree
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
    
    