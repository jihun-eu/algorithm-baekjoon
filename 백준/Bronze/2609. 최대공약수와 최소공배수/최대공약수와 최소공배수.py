#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_gcd(num1, num2):
    if (num2 == 0):
        return num1
    return get_gcd(num2, num1 % num2)

def main():
    num1, num2 = map(int, input().split())
    gcd = get_gcd(max(num1, num2), min(num1, num2))
    lcm = num1 * num2 // gcd

    print(gcd)
    print(lcm)
    

    
    
    

if __name__ == "__main__":
    main()
