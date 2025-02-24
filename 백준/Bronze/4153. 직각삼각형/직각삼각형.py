#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    while True:
        lines = list(map(lambda x: int(x) ** 2, input().split()))
        if sum(lines) == 0:
            break
            
        if sum(lines) == max(lines) * 2:
            print("right")
        else:
            print("wrong")
           
if __name__ == "__main__":
    main()