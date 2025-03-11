#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    stack = []
    
    while True:
        string = input().strip()
        if string == '0':
            break
        tmp = ''
        for char in string:
            stack.append(char)
        while stack:
            tmp += stack.pop()
        if string == tmp:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()