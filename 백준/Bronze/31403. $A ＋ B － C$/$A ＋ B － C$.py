import sys

input = sys.stdin.readline

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    print(A + B - C)
    print(int(str(A) + str(B)) - C)

if __name__ == "__main__":
    main()