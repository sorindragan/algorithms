class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        print("List:")
        node = self
        while node.next:
            print(node.val)
            node = node.next
        print(node.val)

    def add(self, val):
        node = self
        while node.next:
            node = node.next
        new_node = Node(val)
        node.next = new_node

    def remove(self, val):
        node = self
        prev = self
        if node.val == val:
            self = node.next
            self.next = node.next.next
            node.next = None
            return self
        else:
            while node.val != val:
                prev = node
                node = node.next
            if node.next:
                prev.next = node.next
                node.next = None
            else:
                prev.next = None
        return self

def main():
    l = Node(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.traverse()
    l = l.remove(4)
    l = l.remove(1)
    l.traverse()


if __name__ == '__main__':
    main()
