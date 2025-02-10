import sys

input = sys.stdin.readline

def print_star2(num: int) -> str:
    for n in range(1, num + 1):
        print(' '*(num-n)+'*'*n)

def main():
    num = int(input())
    print_star2(num)

if __name__ == "__main__":
    main()