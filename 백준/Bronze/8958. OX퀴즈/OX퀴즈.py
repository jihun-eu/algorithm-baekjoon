import sys

input = sys.stdin.readline

def score_ox_quiz(answers: str) -> int:

    score = 0
    tmp = 0
    for answer in answers:
        if answer == "X": tmp = 0
        else: tmp += 1
        score += tmp
    return score

def main():
    test = int(input())
    for _ in range(test):
        answers = input().rstrip()
        result = score_ox_quiz(answers)
        print(result)

if __name__ == '__main__':
    main()