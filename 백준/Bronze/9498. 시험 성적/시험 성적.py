import sys

input = sys.stdin.readline

def get_grade(score: int) -> str:
    if score < 60: return "F"
    elif score < 70: return "D"
    elif score < 80: return "C"
    elif score < 90: return "B"
    else: return "A"

def main():
    score = int(input())
    result = get_grade(score)
    print(result)

def test():
    assert get_grade(100) == 'A'
    assert get_grade(70) == 'C'

if __name__ == "__main__":
    main()
    # test()