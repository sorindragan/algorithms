class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:

    def __init__(self, init_val=None):
        self.head = Node(init_val)

    def stack_status(self):
        print("Stack:")
        node = self.head
        while node.next:
            print(node.val)
            node = node.next
        print(node.val)

    def push(self, val):
        node = self.head
        if not node.val:
            node.val = val
            return node
        new_node = Node(val)
        new_node.next = node
        self.head = new_node

    def pop(self):
        node = self.head
        pop_val = node.val
        node.val = None
        if node.next:
            node = node.next
            self.head = node
            return pop_val
        return pop_val
        
        

def main():
    stack = Stack(1)
    v = stack.pop()
    print("pop:", v)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.stack_status()
    v = stack.pop()
    print("pop:", v)
    stack.stack_status()
    v = stack.pop()
    print("pop:", v)
    stack.stack_status()


if __name__ == '__main__':
    main()
