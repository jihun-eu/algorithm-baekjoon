#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    sequence = list(map(int, input().split()))
    length = len(sequence)

    compares = 0
    for i in range(1, length):
        if sequence[i-1] < sequence[i]:
            if compares < 0:
                print("mixed")
                return
            compares += 1

        else:
            if compares > 0:
                print("mixed")
                return
            compares -= 1

    if compares < 0:
        print("descending")
    else:
        print("ascending")
            


if __name__ == "__main__":
    main()