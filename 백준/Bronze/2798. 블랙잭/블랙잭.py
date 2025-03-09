#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# nCr = n-1Cr + n-1Cr-1

def nested_for_loop(arr: list, length: int, maximum: int):
    result = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                value = arr[i]+arr[j]+arr[k]
                if value > maximum:
                    continue
                else:
                    result = max(result, value)
    return result

def main():
    length, maximum = map(int, input().split())
    arr = list(map(int, input().split()))
    result = nested_for_loop(arr, length, maximum)
    print(result)

if __name__ == "__main__":
    main()
