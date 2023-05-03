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

    def delete(self, data):
        if self.key is None:
            print("The bst is empty!!")
        elif self.key > data:
            if self.left_child:
                self.left_child = self.left_child.delete(data)
            else:
                print("the node is not present in the bst!!")
        elif self.key < data:
            if self.right_child:
                self.right_child = self.right_child.delete(data)
            else:
                print("The node is not present in the bst!!")
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            else:
                node = self.right_child
                while node.left_child:
                    node = node.left_child
                self.key = node.key
                self.right_child = self.right_child.delete(node.key)
        return self

    def preorder(self):
        print(self.key, end="  ")
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


root = BinarySearchTree(None)
list1 = [8, 3, 12, 9, 10, 2, 5, 7]
for i in list1:
    root.insert(i)

print("pre-order (before delete)")
root.preorder()
root.delete(7)
print("pre-order (before delete)")
root.preorder()
