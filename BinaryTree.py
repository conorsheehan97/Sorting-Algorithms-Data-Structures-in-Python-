class TreeNode: #Creating a TreeNode class for each node in the binary tree
    def __init__(self, value):
        self.value = value # Object attributes are fairly intuitive!
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None # Constructor method

    def insert_value(self, value):
        if self.root is None: # If our tree is empty we may aswell begin at the beginning
            self.root = TreeNode(value)
        self._insert_value_recursive(self.root, value) # See the below method

    def _insert_value_recursive(self, node, value): # Private Helper method for insert_value
        #Two cases here, where the value is bigger/smaller than the node value in question
        #We need to satisfy the condition nodes left child < node < nodes right child
        if value > node.value:
            if node.right is None: # If the right child is empty, we may aswell throw the node here
                node.right = TreeNode(value)  # Instantiating our node
            else: # We recursively work our way down the tree, where our value dictates our direction
                self._insert_value_recursive(node.right, value)

        if value < node.value: # The mirror of what we did above
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_value_recursive(node.left, value)

    def search_value(self, value): # A method to check if a value is within the tree
        return self._search_value_recursive(self.root, value)  # returning the output of the helper method

    def _search_value_recursive(self, node, value):
        if node is None or node.value == value:
            return node # If our tree is empty, or we've found the value, we return None or the node object respectively
        if value < node.value: # our value dictates how we move down the tree
            return self._search_value_recursive(node.left, value)
        return self._search_value_recursive(node.right, value) # recursively calling the helper method whose parameters are dependant on direction of travel
    def traverse_tree(self):
        traversal = [] # a method, using a private helper method, which lists our tree elements in increasing order
        self._traverse_tree_recursive(self.root, traversal) # we start at the root
        return traversal

    def _traverse_tree_recursive(self, node, traversal):
        if node: # continuing on until this evaluates to false
            self._traverse_tree_recursive(node.left, traversal)
            traversal.append(node.value)
            self._traverse_tree_recursive(node.right, traversal)
    # The order above is important, as we work down the left of the tree first. Using the binary
    # tree property. This allows us to append in increasing order. If lines 48,49, & 50 were in reverse order we
    # would be reversing the lst order

# Example usage:
tree = BinaryTree()
tree.insert_value(5)
tree.insert_value(3)
tree.insert_value(7)
tree.insert_value(2)
tree.insert_value(4)
tree.insert_value(6)
tree.insert_value(8)

print(tree.traverse_tree())  # Output: [2, 3, 4, 5, 6, 7, 8]