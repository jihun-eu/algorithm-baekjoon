#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    subjects_num = int(input())
    scores = list(map(int, input().split()))

    avg = sum(scores) / subjects_num / max(scores) * 100
    print(avg)

if __name__ == "__main__":
    main()