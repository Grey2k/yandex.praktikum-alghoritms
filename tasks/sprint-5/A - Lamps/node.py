class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right: Node = right
        self.left: Node = left
