from random import randint;


def generate():
    x = randint(0, 1);
    y = randint(0, 1);
    if x == 0 and y == 1:
        return generate();
    else:
        return x + y;


x = 0;
y = 0;
z = 0;
for i in range(1, 1000000):
    gen = generate();
    if gen == 0:
        x += 1;
    elif gen == 1:
        y += 1;
    else:
        z += 1;

print(x / 1000000);
print(y / 1000000);
print(z / 1000000);
