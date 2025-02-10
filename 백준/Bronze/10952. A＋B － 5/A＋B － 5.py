import sys

def main():
    for line in sys.stdin:
        num1, num2 = map(int, line.split())
        if num1 == num2 == 0: break
        result = num1 + num2
        print(result)

if __name__ == "__main__":
    main()