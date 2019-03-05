def bsmodifiedFirst(arr, low, high, ele):
    if high >= low:
        mid = low + (high - low) // 2;
        if (mid == 0 or ele > arr[mid - 1]) and arr[mid] == ele:
            return mid;
        elif arr[mid] > ele:
            return bsmodifiedFirst(arr, low, mid - 1, ele);
        else:
            return bsmodifiedFirst(arr, mid + 1, high, ele);
        return -1;


def bsmodifiedlast(arr, low, high, ele):
    if high >= low:
        mid = low + (high - low) // 2;
        if (mid == len(arr) - 1 or ele < arr[mid + 1]) and arr[mid] == ele:
            return mid;
        elif ele < arr[mid]:
            return bsmodifiedlast(arr, low, mid - 1, ele);

        else:
            return bsmodifiedlast(arr, mid + 1, high, ele);

        return -1;


arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9];
# print("first postion is :: ", bsmodifiedlast(arr, 0, len(arr) - 1, 6));
print("total :: ", bsmodifiedlast(arr, 0, len(arr) - 1, 6) - bsmodifiedFirst(arr, 0, len(arr) - 1, 6) + 1);
