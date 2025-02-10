import sys

input = sys.stdin.readline

def getSum(a: int, b: int) -> int:
    bitmask = 0xffffffff
    while b & bitmask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a


def main():
    a, b = map(int, input().split())
    result = getSum(a, b)
    print(result)


if __name__ == "__main__":
    main()