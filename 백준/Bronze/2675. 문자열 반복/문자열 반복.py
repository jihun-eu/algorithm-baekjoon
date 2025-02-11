import sys

input = sys.stdin.readline

def repeat_n(n: int, string: str) -> str:
    new_string = ""
    for char in string:
        new_string += char * n

    return new_string

def main():
    case = int(input())
    for _ in range(case):
        n, string = input().split()
        result = repeat_n(int(n), string)
        print(result)

if __name__ == '__main__':
    main()