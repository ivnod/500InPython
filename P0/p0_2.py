def isZeroSumPresent(arr, arr_len):
    sum = 0;
    s = set();
    for i in range(0, arr_len):
        sum = sum + arr[i];
        if arr[i] == 0 or sum in s:
            print("Zero sum present  ", i);
            break;
        else:
            s.add(sum);


arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2];

isZeroSumPresent(arr, len(arr));
