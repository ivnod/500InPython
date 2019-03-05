def bs(array, low, high, ele):
    mid = low + (high - low) // 2;
    if array[mid] == ele:
        return mid;
    elif array[mid] > ele:
        return bs(array, low, mid - 1, ele);
    elif array[mid] < ele:
        return bs(array, mid + 1, high, ele);
    return -1;


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
index = bs(arr, 0, len(arr), 9);

print("index is ::: ", index)
