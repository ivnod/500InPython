def isCircular(str):
    x = 0;
    y = 0;
    dir = "N";
    for i in range(0, len(str)):

        if str[i] == "M":
            if dir == "N":
                y += 1;
            elif dir == "S":
                y -= 1;

            elif dir == "W":
                x -= 1;
            else:
                x += 1;
        elif str[i] == "L":
            if dir == "N":
                dir = "W";
            elif dir == "S":
                dir = "E";
            elif dir == "E":
                dir = "N"
            else:
                dir = "S";
        else:
            if dir == "N":
                dir = "E";
            elif dir == "S":
                dir = "W";
            elif dir == "E":
                dir = "S"
            else:
                dir = "N";
    print(x, y)
    return x == 0 and y == 0;`


str = "MMRMMRMMRMML";

if isCircular(str):
    print("Cicular");
else:
    print("Not circular");
