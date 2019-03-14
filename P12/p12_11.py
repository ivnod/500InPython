from P12.LinkedList import LinkedList


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


list = LinkedList();
list.add_list_item(1);
list.add_list_item(2);
list.add_list_item(3);
list.add_list_item(4);
list.add_list_item(5);
list.printlist();
print("");
reverse(list);
list.printlist();
