class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


def printlist(headnode):
    curr = headnode;
    while curr != None:
        print(curr.data, end=" ");
        curr = curr.next;


def reverse(headnode):
    prev = None;
    curr = headnode;
    next = headnode;
    while curr != None:
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    return prev;


head = Node(1);
head.next = Node(2);
head.next.next = Node(3);
head.next.next.next = Node(4);
head.next.next.next.next = Node(5);

printlist(head);

head = reverse(head);

print("");
printlist(head);
