from random import randint;


def generate():
    return randint(0, 1) & randint(0, 1);


x = 0;
y = 0;
for i in range(1, 1000000):
    if generate() == 0:
        x += 1;
    else:
        y += 1;

print(x / 1000000);
print(y / 1000000);
