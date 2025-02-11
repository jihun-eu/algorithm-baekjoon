#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    
    num_list = [0]*10
   
    MAX_NUMS = 3
    num = 1
    for _ in range(MAX_NUMS):
        num *= int(input())

    num_string = str(num)
    for n in num_string:
        num_list[int(n)] += 1

    for n in num_list:
        print(n)

if __name__ == "__main__":
    main()