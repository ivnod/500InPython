def division(a, b):
    den = b;
    quo = 1;
    while den < a:
        den *= 2;
        quo *= 2;
    while den > a:
        den = den - a;
        quo = quo - 1;
    return quo;


print(division(22, 7))
