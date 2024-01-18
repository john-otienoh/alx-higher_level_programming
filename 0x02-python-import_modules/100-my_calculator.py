#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argv_len = len(argv)
    if argv_len - 1 < 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if argv[2] == '+':
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif argv[2] == '/':
            a = int(argv[1])
            b = int(argv[3])
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
