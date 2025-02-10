import sys

input = sys.stdin.readline

def is_leap_year(year: int) -> int:
    return int(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

def main():
    year = int(input())
    result = is_leap_year(year)
    print(result)

if __name__ == "__main__":
    main()