import sys

input = sys.stdin.readline

def compareTwoNums(num1: int, num2: int) -> str:
    if num1 == num2: return "=="
    if num1 < num2: return "<"
    else: return ">"
    
def main():
    num1, num2 = map(int, input().split())
    result = compareTwoNums(num1, num2)
    print(result)
    
if __name__ == "__main__":
    main()