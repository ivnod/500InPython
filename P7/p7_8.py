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


def minKey(root):
    if root.right != None:
        root = root.right;
    return root;


def deleteNode(root, key):
    if root == None:
        return root;
    if (key < root.data):
        return deleteNode(root.left, key);
    elif (key > root.data):
        return deleteNode(root.right, key);
    else:
        if root.left == None and root.right == None:
            return None;
        elif root.left != None and root.right != None:
            pre = minKey(root.left);
            root.data = pre.data;
            deleteNode(root.left, pre.data);
        else:
            child = root.left if root.left != None else root.right;
            root = child;
    return root;


arr = [15, 10, 20, 8, 12, 16, 25];
root = None;
for i in range(len(arr)):
    root = insert(root, arr[i])

inorder(root);
root = deleteNode(root, 12);
inorder(root);
