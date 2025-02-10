import sys

input = sys.stdin.readline

def main():
    num = int(input())
    print(sum(int(n) for n in input().rstrip()))

if __name__ == "__main__":
    main()