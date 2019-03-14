def printPairs(arr, arr_size, sum):
    S = set();
    for i in range(arr_size):
        ele = sum - arr[i];
        if ele >= 0 and ele in S:
            print(ele, " ", arr[i]);
            break;
        else:
            S.add(arr[i]);


arr = [1, 4, 45, 6, 10, 8];
sum = 16;
printPairs(arr, len(arr), sum);
