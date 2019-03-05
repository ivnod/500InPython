def bsmodified(arr, low, high):
    if high >= low:
        if arr[low] <= arr[high]:
            return low;
        mid = low + (high - low) // 2;
        prev = (mid - 1 + len(arr)) % len(arr);
        next = (mid + 1) % len(arr);
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid;
        elif arr[mid] <= arr[high]:
            return bsmodified(arr, low, mid - 1);
        elif arr[mid] >= arr[low]:
            return bsmodified(arr, mid + 1, high);
        return -1;


arr = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7];
print("rorations are :: ", bsmodified(arr, 0, len(arr) - 1));
