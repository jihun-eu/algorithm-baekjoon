#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():

    MAX_NUM = 1001

    num_count = int(input())
    nums = list(map(int, input().split()))

    is_prime = [i > 1 for i in range(MAX_NUM)]

    for num in range(2, int(max(nums) ** 0.5) + 1):
        for i in range(2*num, MAX_NUM, num):
            is_prime[i] = False

    for num in nums:
        if not is_prime[num]:
            num_count -= 1

    print(num_count)




if __name__ == "__main__":
    main()