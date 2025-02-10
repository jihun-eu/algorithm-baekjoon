#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num1, num2 = map(int, input().split())

    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1//num2)
    print(num1%num2)

if __name__ == "__main__":
    main()