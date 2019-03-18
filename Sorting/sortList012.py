from P12.LinkedList import LinkedList;


def sort(list):
    curr = list;
    zero = LinkedList();
    one = LinkedList();
    two = LinkedList();
    zero = one = two = curr;
    while curr is not None:
        if curr.data == 0:
            zero = curr;
            zero.next = curr.next;
        elif curr.data == 1:
            one = curr;
            one.next = curr.next;
        else:
            two = curr;
            two.next = curr.next;
        curr = curr.next;
    zero.next = one;
    one.next = two;
    two.next = None;
    return zero;


list = LinkedList();
list.add_list_item(1);
list.add_list_item(2);
list.add_list_item(0);
list.add_list_item(0);
list.add_list_item(1);
list.add_list_item(2);
list.add_list_item(1);
list.add_list_item(2);
list.add_list_item(1);
list.printlist();

list = sort(list.head);

