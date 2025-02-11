#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    case = int(sys.stdin.readline())

    for _ in range(case):
        floor, _, guest = map(int, sys.stdin.readline().strip('\n').split())
        tmp = guest % floor * 100 + guest // floor + 1
        if guest % floor == 0:
            tmp = floor * 100 + guest // floor
        print(tmp)


if __name__ == "__main__":
    main()