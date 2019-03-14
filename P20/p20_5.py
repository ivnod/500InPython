def setBothZeroes(arr):
    arr[arr[1]] = arr[arr[0]];
    return arr;


print(setBothZeroes([1, 0]));
