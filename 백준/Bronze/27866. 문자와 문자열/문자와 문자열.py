import sys

input = sys.stdin.readline

def get_ith_char(string: str, idx: int) -> str:
    return string[idx-1]

def main():
    string = input().rstrip()
    idx = int(input())
    result = get_ith_char(string, idx)
    print(result)

def test():
    assert get_ith_char('Sprout', 3) == 'r'
    assert get_ith_char('shiftpsh', 6) == 'p'

if __name__ == "__main__":
    main()
    # test()