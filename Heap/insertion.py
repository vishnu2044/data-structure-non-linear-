class MinHeap:
    def __init__(self, limit):
        self.array = []
        self.limit = limit
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child(index) < self.size

    def parent_value(self, index):
        return self.array[self.get_parent_index(index)]

    def left_child_value(self, index):
        return self.array[self.get_left_child_index(index)]

    def right_child_value(self, index):
        return self.array[self.get_right_child_index(index)]

    def is_full(self):
        return self.size == self.limit

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def insert(self, data):
        self.array.append(data)
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self, index):
        if self.has_parent(index) and self.array[index] < self.parent_value(index):
            self.swap(index, self.get_parent_index(index))
            self.heapify_up(self.get_parent_index(index))


list1 = [7, 5, 0, 2, 4, 10, 9]
myheap = MinHeap(len(list1))
for i in list1:
    myheap.insert(i)

print(myheap.array)
