def bsmodified(arr, low, high, ele):
    if high >= low:
        mid = low + (high - low) // 2;
        if (mid == 0 or ele > arr[mid - 1]) and arr[mid] == ele:
            return mid;
        elif arr[mid] > ele:
            return bsmodified(arr, low, mid - 1, ele);
        elif arr[mid] < ele:
            return bsmodified(arr, mid + 1, high, ele);
        return -1;


arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9];
print("first postion is :: ", bsmodified(arr, 0, len(arr) - 1, 5));
