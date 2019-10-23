#!/usr/bin/python
from random import randint

def main():
    min = 1
    max = 6
    num1 = randint(min, max)
    num2 = randint(min, max)
    print randint(num1 + num2)

if __name__ == '__main__':
    main()