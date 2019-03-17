from random import randint;


def biased():
    x = randint(1, 100);
    if x < 80:
        return 0;
    else:
        return 1;


def generate():
    while True:
        first = biased();
        second = biased();

        if first != second:
            return first;


x = 0;
y = 0;

for i in range(1, 100000):

    val = generate();
    if val == 0:
        x += 1;
    else:
        y += 1;

print(x / 1000000)
print(y / 1000000)
