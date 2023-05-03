class BinaryTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        elif self.left_child is None:
            self.left_child = BinaryTree(data)
        elif self.right_child is None:
            self.right_child = BinaryTree(data)
        else:
            if self.key > data:
                if self.left_child:
                    self.left_child.insert(data)
            else:
                if self.right_child:
                    self.right_child.insert(data)


tree = BinaryTree(5)

tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left_child)
        print(root.key)
        inorder_traversal(root.right_child)


inorder_traversal(tree)


