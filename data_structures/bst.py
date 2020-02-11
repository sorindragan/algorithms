class Node:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
class BST:

    def __init__(self):
        self.root = Node()

    def add(self, value, root=None):
        if not root:
            root = self.root

        if not root.value:
            root.value = value
        else:
            if value < root.value:
                if not root.left:
                    root.left = Node(value)
                else:
                    self.add(value, root.left)
            if value > root.value:
                if not root.right:
                    root.right = Node(value)
                else:
                    self.add(value, root.right)
    
    @staticmethod
    def find_replace_value(node):
        left_option = None
        right_option = None
        # TODO: find possible replacement values
        #       decide between them and delete the chosen node

        return 0


    def delete(self, value):
        node = self.root
        to_del = None

        if node.value == value:
            to_del = node
            # TODO: check if node is a leaf or not
            replace_val = find_replace_value(to_del)
            return
        
        self.delete(node.left)
        self.delete(node.right)
    
    def level_traversal(self):
        root = self.root

        order_q = [root]
        while order_q:
            node = order_q.pop(0)
            print("NAN" if not node.value else node.value)
        
            if node.left:
                order_q.append(node.left)
            if node.right:
                order_q.append(node.right)
    
    def inorder_traversal(self, root="start"):
        if root=="start":
            root = self.root

        if root:
            self.inorder_traversal(root.left)
            print(root.value)
            self.inorder_traversal(root.right)


def main():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(6)
    bst.add(9)
    bst.add(4)
    bst.add(1)
    bst.level_traversal()
    print("--------------------------------")
    bst.inorder_traversal()


if __name__ == '__main__':
    main()
