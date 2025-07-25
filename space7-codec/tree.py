class TreeNode:
    def __init__(self, data=-1):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def __repr__(self):
        return f"<{self.data} - [{self.left}, {self.right}]>"