import sys

input = sys.stdin.readline

def main():
    maximum, pos = -1, -1
    for i in range(9):
        num = int(input())
        if maximum < num:
            maximum = num
            pos = i

    print(maximum)
    print(pos+1)

if __name__ == "__main__":
    main()