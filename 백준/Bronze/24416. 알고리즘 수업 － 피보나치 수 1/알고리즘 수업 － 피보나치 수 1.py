import sys

input = sys.stdin.readline

def count_fib_computation(num: int) -> int:
    dp_fib_cnt = num - 2
    
    recursive_fib_cnt, tmp = 1, 1
    for _ in range(3, num+1):
        tmp, recursive_fib_cnt = recursive_fib_cnt, recursive_fib_cnt + tmp
        
    return recursive_fib_cnt, dp_fib_cnt

def main():
    num = int(input())
    recursive_fib_cnt, dp_fib_cnt = count_fib_computation(num)
    print(recursive_fib_cnt, dp_fib_cnt)
    
if __name__ == "__main__":
    main()