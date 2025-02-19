import sys
from typing import List

input = sys.stdin.readline

def length_of_line(num: int, lines: List[List[int]]) -> int:
    length = 0

    lines.sort()

    newLine = lines[0]
    for line in lines[1:]:
        if newLine[1] < line[0]:
            length += newLine[1] - newLine[0]
            newLine = line
        else:
            newLine[1] = max(newLine[1], line[1])
    length += newLine[1] - newLine[0]

    return length

def main():
    num = int(input())
    lines = list(list(map(int, input().split())) for _ in range(num))
    result = length_of_line(num, lines)
    print(result)

def test():
    assert length_of_line(4, [[1, 3], [2, 5], [3, 5], [6, 7]]) == 5


if __name__ == '__main__':
    main()
