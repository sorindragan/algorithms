import copy
import random

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

    def delete(self, value, root=None):
        if not root:
            node = self.root
        else:
            node = root

        children = [node.left.value if node.left else None, node.right.value if node.right else None]
        to_del = None
        
        if value in children:
            to_del, direction = (node.left, "left") if node.left.value == value else (node.right, "right")

            # print(to_del.left, to_del.right)
            # leaf node 17
            if (not to_del.left) and (not to_del.right):
                if direction == "left":
                    node.left = None
                else:
                    node.right = None
                del(to_del)
                return
                
            # only left child 13
            if to_del.left and not to_del.right:
                node.left = copy.deepcopy(to_del.left)
                del(to_del)
                return
            
            
            # only right child 7
            if not to_del.left and to_del.right:
                node.right = copy.deepcopy(to_del.right)
                del(to_del)
                return
                
            # tree node 5
            if to_del.left and to_del.right:
                lost_values = []
                self.get_children_by_level(to_del, lost_values)
                lost_values.remove(to_del.value)
                # print(lost_values)
                if direction == "left":
                    node.left = None
                else:
                    node.right = None
                del(to_del)
                for val in lost_values:
                    self.add(val)
                return
                       
        if value < node.value:
            self.delete(value, node.left)
        
        if value > node.value:
            self.delete(value, node.right)

            
    def get_children_inorder(self, root, children=[]):
        if root:
            self.get_children(root.left, children)
            children.append(root.value)
            self.get_children(root.right, children)

    def get_children_by_level(self, root, children=[]):
        order_q = [root]
        while order_q:
            node = order_q.pop(0)
            children.append(node.value)

            if node.left:
                order_q.append(node.left)
            if node.right:
                order_q.append(node.right)

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
    bst.add(11)
    bst.add(5)
    bst.add(15)
    bst.add(3)
    bst.add(7)
    bst.add(1)
    bst.add(4)
    bst.add(9)
    bst.add(13)
    bst.add(17)
    bst.add(12)

    print("Level Traversal")
    bst.level_traversal()
    # print("Inorder Traversal")
    # bst.inorder_traversal()
    print("--------------------------------")
    print("DELETING")
    bst.delete(17)
    bst.delete(13)
    bst.delete(5)
    bst.delete(7)
    print("Level Traversal")
    bst.level_traversal()

if __name__ == '__main__':
    main()
