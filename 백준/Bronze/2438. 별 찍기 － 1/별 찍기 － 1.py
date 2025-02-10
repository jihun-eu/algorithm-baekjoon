import sys

input = sys.stdin.readline

def printStar(num: int) -> str:
    string = ''
    for star in range(1, num + 1):
        string += ('*' * star) + '\n'
    return string


def main():
    num = int(input())
    result = printStar(num)
    print(result)


if __name__ == "__main__":
    main()