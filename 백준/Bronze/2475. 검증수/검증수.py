#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    nums = map(lambda x: int(x) ** 2, input().split())
    verified = sum(nums) % 10
    print(verified)
    
if __name__ == "__main__":
    main()