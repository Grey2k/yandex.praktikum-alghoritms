class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right: Node = right
        self.left: Node = left
