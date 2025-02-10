import sys

input = sys.stdin.readline

def getSub(a: int, b: int) -> int:
    return a - b


def main():
    a, b = map(int, input().split())
    result = getSub(a, b)
    print(result)


if __name__ == "__main__":
    main()