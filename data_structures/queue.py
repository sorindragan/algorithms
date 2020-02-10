class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:

    def __init__(self, init_val=None):
        self.head = Node(init_val)

    def queue_status(self):
        print("Queue:")
        node = self.head
        while node.next:
            print(node.val)
            node = node.next
        print(node.val)

    def enqueue(self, val):
        node = self.head
        if not node.val:
            node.val = val
        else:            
            new_node = Node(val)
            new_node.next = node
            self.head = new_node

    def dequeue(self):
        prev = node = self.head
        if not node.next:
            dequeue_val = node.val
            node.val = None
        else:
            while node.next:
                prev = node
                node = node.next
            dequeue_val = node.val
            prev.next = None
            
        return dequeue_val


def main():
    queue = Queue(1)
    v = queue.dequeue()
    print("dequeue:", v)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.queue_status()
    v = queue.dequeue()
    print("dequeue:", v)
    queue.queue_status()
    v = queue.dequeue()
    print("dequeue:", v)
    queue.queue_status()


if __name__ == '__main__':
    main()
