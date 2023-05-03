class BinarySearchTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        elif self.key > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BinarySearchTree(data)
        elif self.key < data:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BinarySearchTree(data)

    def preorder(self):
        print(self.key, end="  ")
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key, end="  ")
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key, end="  ")


root = BinarySearchTree(None)
list1 = [8, 3, 12, 9, 10, 2, 5, 7]
for i in list1:
    root.insert(i)

print("pre-order")
root.preorder()
print("\nin-order")
root.inorder()
print("\npost-order")
root.postorder()