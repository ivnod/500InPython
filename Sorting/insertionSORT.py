def insertionSort(arr):
    for i in range(1, len(arr)):
        value = arr[i];
        j = i;
        while j > 0 and value < arr[j - 1]:
            arr[j] = arr[j - 1];
            j = j - 1;
        arr[j] = value;


def insertionSortRecur(arr, i, n):
    value = arr[i];
    j = i;
    while j > 0 and value < arr[j - 1]:
        arr[j] = arr[j - 1];
        j = j - 1;
    arr[j] = value;
    if i < n - 1:
        insertionSortRecur(arr, i + 1, n);


arr = [3, 8, 5, 4, 1, 9, -2, 10, 6];
print(arr)
insertionSort(arr)
print(arr)
arr = [3, 8, 5, 4, 1, 9, -2, 10, 6, 2, 0, 13];
print(arr)
insertionSortRecur(arr, 1, len(arr));
print(arr)
