def printMaxActivities(s, f):
    n = len(s);
    i = 0;
    print(i);
    for j in range(1, n):
        if s[j] >= f[i]:
            print(j);
            i = j;


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f);


class Activity:
    def __init__(self, start, finish):
        self.start = start;
        self.finish = finish;

    def __str__(self):
        return self.start;


tasks = [Activity(5, 9), Activity(1, 2), Activity(3, 4), Activity(0, 6), Activity(5, 7), Activity(8, 9)]
print(tasks)
