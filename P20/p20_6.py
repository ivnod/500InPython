def min(a, b):
    num = 0;
    while a > 0 and b > 0:
        num += 1;
        a -= 1;
        b -= 1;
    return num;


def minMethodOne(a, b):
    min = (a > b) * b + (a < b) * a;
    return min;


print(min(10, 2));
print(minMethodOne(1, 12));
print(min(12, 12));
print(min(10, 12));
