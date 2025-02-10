import sys

input = sys.stdin.readline

def print_util_n(num: int) -> None:
    for n in range(1, num+1):
        print(n)

def main():
    num = int(input())
    print_util_n(num)

if __name__ == "__main__":
    main()