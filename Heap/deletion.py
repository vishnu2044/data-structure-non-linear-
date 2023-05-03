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
        return self.get_right_child_index(index) < self.size

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
        if self.is_full():
            raise Exception("the heap is full!!")
        self.array.append(data)
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self, index):
        if self.has_parent(index) and self.array[index] < self.parent_value(index):
            self.swap(index, self.get_parent_index(index))
            self.heapify_up(self.get_parent_index(index))

    def delete(self):
        if self.size == 0:
            raise Exception("The heap is empty!!")
        data = self.array[0]
        self.array[0] = self.array.pop()
        self.size -= 1
        self.heapify_down(0)

    def heapify_down(self, index):
        smallest = index
        if (self.has_left_child(index) and self.array[smallest] > self.left_child_value(index)):
            smallest = self.get_left_child_index(index)
        if (self.has_right_child(index) and self.array[smallest] > self.right_child_value(index)):
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)


list1 = [7, 5, 0, 2, 4, 1, 3]
myheap = MinHeap(len(list1))
for i in list1:
    myheap.insert(i)

print(myheap.array)
myheap.delete()
print(myheap.array)
