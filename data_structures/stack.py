class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def stack_status(self):
        print("Stack:")
        node = self
        while node.next:
            print(node.val)
            node = node.next
        print(node.val)

    def push(self, val):
        node = self
        if not node.val:
            node.val = val
            return node
        new_node = Node(val)
        new_node.next = node
        return new_node

    def pop(self):
        node = self
        pop_val = node.val
        if node.next:
            node = node.next
            return pop_val, node
        return pop_val, Node(None)
        
        

def main():
    stack = Node(1)
    v, stack = stack.pop()
    print("pop:", v)
    stack = stack.push(2)
    stack = stack.push(3)
    stack = stack.push(4)
    stack.stack_status()
    v, stack = stack.pop()
    print("pop:", v)
    stack.stack_status()
    v, stack = stack.pop()
    print("pop:", v)
    stack.stack_status()


if __name__ == '__main__':
    main()
