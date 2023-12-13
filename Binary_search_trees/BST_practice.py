class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # method to create a node
    def insert(self, new_data):
        if self.data:
            if new_data < self.data:
                if self.left is None:
                    self.left = Node(new_data)
                else:
                    self.left.insert(new_data)

            elif new_data > self.data:
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    # method to search data
    def search(self, key):
        if key < self.data:
            if self.left is None:
                return "{} is not found".format(key)
            else:
                return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return "{} is not found".format(key)
            else:
                return self.right.search(key)
        else:
            return "{} is found".format(self.data)

root = Node(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)

print(root.search(10))
print(root.search(5))

