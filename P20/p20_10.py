from random import randint;


def generate():
    x = randint(1, 6);
    y = randint(1, 6);
    return (2 * x) - (y & 1);


freq = [0] * 13;

for i in range(1, 1000000):
    x = generate();
    freq[x] += 1;

print(freq)

for i in range(1, len(freq)):
    print(freq[i] / 1000000);
