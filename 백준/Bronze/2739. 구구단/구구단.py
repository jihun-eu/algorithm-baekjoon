import sys

input = sys.stdin.readline

def print_mult_table(num: int) -> None:
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")

def main():
    num = int(input())
    print_mult_table(num)

if __name__ == "__main__":
    main()