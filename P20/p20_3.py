def square(a):
    res = 0;
    for i in range(1, a + 1):
        res = res + a;
    return res;


def bitwisesquare(a):
    if (a < 2):
        return a;
    i = a >> 1;
    if a & 1 == 1:
        return ((bitwisesquare(i) << 2) + (i << 2) + 1);
    else:
        return (bitwisesquare(i) << 2);


for i in range(1, 20):
    print(square(i))

for i in range(1, 20):
    print(bitwisesquare(i))
