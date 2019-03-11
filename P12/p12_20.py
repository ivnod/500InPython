class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


def printlist(headNode):
    curr = headNode;
    while curr != None:
        print(curr.data, end=" ");
        curr = curr.next;


def rearrange(headNode):
    curr = headNode;
    while curr.next.next != None:
        curr = curr.next;
    curr.next.next = headNode;
    head = curr.next;
    curr.next = None;
    return head;


head = Node(1);
head.next = Node(2);
head.next.next = Node(3);
head.next.next.next = Node(4);
head.next.next.next.next = Node(5);

printlist(head);

head = rearrange(head);
printlist(head);
