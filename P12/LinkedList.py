from P12.Node import Node


class LinkedList:
    def __init__(self):
        " constucting LinkedList"
        self.head = None;
        self.tail = None;
        return

    def add_list_item(self, item):
        "add an item"
        if not isinstance(item, Node):
            item = Node(item);
        if self.head is None:
            self.head = item;
        else:
            self.tail.next = item;
        self.tail = item;
        return

    def list_length(self):
        "return no of elements in list"
        count = 0;
        current_node = self.head;
        while current_node is not None:
            count = count + 1;
            current_node = current_node.next;
        return count;

    def printlist(self):
        "output list"
        current_node = self.head;
        while current_node is not None:
            print(current_node.data, end=" ");
            current_node = current_node.next;
        return;
