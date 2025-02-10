import sys

input = sys.stdin.readline

def getDiv(a: int, b: int) -> int:
    return a / b


def main():
    a, b = map(int, input().split())
    result = getDiv(a, b)
    print(result)


if __name__ == "__main__":
    main()