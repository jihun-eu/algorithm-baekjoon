#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    num = int(input())

    result = 1
    for n in range(num):
        num -= 6 * n if 6 * n > 0 else 1
        if num <= 0:
            result += n
            break
            
    
    print(result)
    
    

if __name__ == "__main__":
    main()
