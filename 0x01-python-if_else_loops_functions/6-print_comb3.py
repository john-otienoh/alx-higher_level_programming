#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print("{}".format(i), end="")
            print("{}".format(j), end="")
            if i  != 8 and i != 9:
                print(", ", end="")
