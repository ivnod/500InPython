def multiplybyrecursion(a, b):
    if (a == 0 or b == 0):
        return 0;
    if (b == 1):
        return a;
    return a + multiplybyrecursion(a, b - 1);


print(multiplybyrecursion(1, 2));


def bitLogicMul(a, b):
    res = 0;
    while (b != 0):
        if b & 1 != 0:
            res += a;
        a = a << 1;
        b = b >> 1;
    return res;


print(bitLogicMul(8, 9));
