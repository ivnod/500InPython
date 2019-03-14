from .Node import Node


def reverse(headnode):
    if headnode == None:
        return;
    if headnode.next == None:
        return headnode;
    reverse(headnode.next);
    headnode.next.next = headnode;
    headnode.next = None;


head = Node(1);
head.next = Node(2);
head.next.next = Node(3);
head.next.next.next = Node(4);
head.next.next.next.next = Node(5);

printlist(head);

head = reverse(head);

print("");
printlist(head);
