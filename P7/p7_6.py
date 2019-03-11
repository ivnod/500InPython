class Node:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;


def insert(root, key):
    if root == None:
        return Node(key);
    if key < root.data:
        root.left = insert(root.left, key);
    else:
        root.right = insert(root.right, key);
    return root;


def inorder(root):
    if root == None:
        return;
    inorder(root.left);
    print(root.data, end=" ");
    inorder(root.right);


arr = [15, 10, 20, 8, 12, 16, 25];
root = None;
for i in range(len(arr)):
    root = insert(root, arr[i])

inorder(root);
