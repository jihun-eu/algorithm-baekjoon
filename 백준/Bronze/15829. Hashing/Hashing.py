#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    r = 31
    num = int(input())
    string = input()

    result = 0

    for i in range(num):
        result += (ord(string[i]) - 96) * (r ** (i))

    print(result % 1234567891)

if __name__ == "__main__":
    main()