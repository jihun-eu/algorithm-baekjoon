import sys

input = sys.stdin.readline

def count_alphabets(string: str) -> str:

    unicode_a = 97
    alphabets = [-1] * 26

    for i in range(len(string)):
        index = ord(string[i]) - unicode_a
        if alphabets[index] != -1: continue
        alphabets[index] = i

    return " ".join([str(i) for i in alphabets])

def main():
    string = input().rstrip()
    result = count_alphabets(string)
    print(result)

if __name__ == '__main__':
    main()