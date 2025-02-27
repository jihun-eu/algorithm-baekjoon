#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

def main():
    participants = int(sys.stdin.readline().rstrip())
    sizes = list(map(int, sys.stdin.readline().rstrip().split()))
    pack_shirt, pack_pen = map(int, sys.stdin.readline().rstrip().split())

    pack_of_shirts_to_buy = sum([math.ceil(s / pack_shirt) for s in sizes])
    pack_of_pens_to_buy = participants // pack_pen
    single_pens_to_buy = participants % pack_pen

    print(pack_of_shirts_to_buy)
    print(pack_of_pens_to_buy, single_pens_to_buy)
    


if __name__ == "__main__":
    main()