#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    count = int(input())

    nums = list(map(int, input().split()))
    assert len(nums) == count, len(nums)

    print(min(nums), max(nums))

if __name__ == "__main__":
    main()

