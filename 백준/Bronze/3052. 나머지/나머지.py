#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    TURN = 10
    MODULO = 42
    
    unique_remainder_count = 0
    unique_remainder = [0] * MODULO
    for _ in range(TURN):
        num = int(input())
        if unique_remainder[num % MODULO] == 0:
            unique_remainder_count += 1
            unique_remainder[num % MODULO] += 1
        
    print(unique_remainder_count)

if __name__ == "__main__":
    main()
    

        