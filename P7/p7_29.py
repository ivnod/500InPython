def bsmodified(arr, low, high):
    if low > high:
        return low;
    mid = low + (high - low) // 2;
    if arr[mid] == mid:
        return bsmodified(arr, mid + 1, high);
    else:
        return bsmodified(arr, low, mid - 1);


arr = [0, 1, 2, 3, 4, 5, 6];
print(bsmodified(arr, 0, len(arr) - 1));
