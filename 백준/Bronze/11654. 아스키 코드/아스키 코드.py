import sys

input = sys.stdin.readline

def is_leap_year(char: str) -> int:
    return ord(char)

def main():
    char = input().rstrip()
    result = is_leap_year(char)
    print(result)

def test():
    assert is_leap_year('A') == 65
    assert is_leap_year('C') == 67
    assert is_leap_year('0') == 48

if __name__ == "__main__":
    main()
    # test()