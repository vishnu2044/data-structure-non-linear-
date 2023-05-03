class BinarySearchTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.key in None:
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


root = BinarySearchTree(None)
list1 = [8, 3, 12, 9, 10, 2, 5, 7]
for i in list1:
    root.insert(i)
