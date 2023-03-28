class DLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        if self.next and self.next.key is not None:
            return f"{self.key}:{self.value},{str(self.next)}"
        elif self.key:
            return f"{self.key}:{self.value}]"
        else:
            return "]"

class DoublyLinkedList:
    def __init__(self):
        self.head = DLNode(None, None)
        self.tail = DLNode(None, None)
        self.curr = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0
    
    def move_to_end(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        curr_end_node = self.tail.prev

        curr_end_node.next = node
        node.prev = curr_end_node
        node.next = self.tail
        self.tail.prev = node

    def add(self, key, value):
        node = DLNode(key, value)
        self.curr.next.prev = node
        node.next = self.curr.next
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        self.len += 1
        return node

    def pop(self):
        if self.head.next != self.tail:
            node = self.head.next
            node.next.prev = self.head
            self.head.next = node.next
            if node == self.curr:
                self.curr = self.head
            node.next = None
            node.prev = None
            self.len -= 1
            return node
        else:
            return None
    
    def __len__(self):
        return self.len

    def __str__(self):
        return "[" + str(self.head.next)
    
    
if __name__ == '__main__':
    l = DoublyLinkedList()
    l.add("a", 5)
    b_node = l.add("b", 3)
    l.add("c", 6)
    print(l)
    node = l.pop()
    print(node)
    print(l)

    l.move_to_end(b_node)
    print(l)

    print("======================")

    l = DoublyLinkedList()
    node = l.add("a", 2)
    node.value = 4
    l.move_to_end(node)
    print(l)
    

