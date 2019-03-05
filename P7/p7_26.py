def bsmodified(arr, low, high, ele):
    if high >= low:
        mid = low + (high - low) // 2;
        if arr[mid] == ele:
            return mid;
        if arr[mid] <= arr[high]:
            if arr[mid] < ele <= arr[high]:
                return bsmodified(arr, mid + 1, high, ele);
            else:
                return bsmodified(arr, low, mid - 1, ele);
        else:
            if arr[low] < ele < arr[mid]:
                return bsmodified(arr, low, mid - 1, ele);
            else:
                return bsmodified(arr, mid + 1, high, ele);
        return -1;


arr = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7];
print("rorations are :: ", bsmodified(arr, 0, len(arr) - 1, 1));
