# Ben Lizza
# 03/02/20


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def push_head(self, data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def push_tail(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            self.head.prev = None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def pop_head(self):
        curr = self.head
        self.head.next.prev = None
        self.head = self.head.next
        return curr.data

    def pop_tail(self):
        curr = self.head
        if curr.next is None:
            self.head = None
        while curr.next:
            curr = curr.next
            self.head = curr
            curr.prev = None


