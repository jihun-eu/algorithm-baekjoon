import sys
import math
from typing import List, Tuple

input = sys.stdin.readline

def getDigit(num: int) -> int:
    return math.floor(math.log10(num)) + 1

def sumDecomposition(num: int) -> int:
    digitSum = 0
    origNum = num
    while num > 0:
        digitSum += num % 10
        num //= 10
    return origNum + digitSum

def getPrevDecomposition(num: int) -> int:
    digit = getDigit(num)
    minNum = num - (digit * 9)
    for constructor in range(minNum, num):
        if sumDecomposition(constructor) == num:
            return constructor
    return 0

def main():
    num = int(input())
    result = getPrevDecomposition(num)
    print(result)


if __name__ == "__main__":
    main()