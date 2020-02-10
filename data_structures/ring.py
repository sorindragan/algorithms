class Node:
    
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Ring:

    def __init__(self, size):
        self.size = size
        self.insertIdx = 0
        count = 0
        self.head = Node()
        node = self.head
        while count < size - 1:
            count += 1
            new_node = Node()
            node.next = new_node
            node = new_node
        
        node.next = self.head
    
    def traverse(self):
        print("Ring:")
        node = self.head
        while node.next != self.head:
            print(node.value)
            node = node.next
        print(node.value)

    def add(self, val):
        node = self.head
        count = 0
        while count < self.insertIdx:
            node = node.next
            count += 1
        node.value = val
        self.insertIdx = (count + 1) % self.size
    
    def remove(self):
        node = self.head
        count = 0
        if self.insertIdx != 0:
            self.insertIdx -= 1
        while count < self.insertIdx:
            node = node.next
            count += 1
        node.value = None
       


def main():
    ring = Ring(5)
    ring.traverse()
    ring.add(1)
    ring.add(2)
    ring.add(3)
    ring.add(4)
    ring.add(5)
    ring.traverse()
    ring.add(6)
    ring.add(7)
    ring.add(8)
    ring.add(9)
    ring.traverse()
    ring.remove()
    ring.remove()
    ring.traverse()
    ring.add(10)
    ring.add(11)
    ring.add(12)
    ring.add(13)
    ring.traverse()

if __name__ == '__main__':
    main()
