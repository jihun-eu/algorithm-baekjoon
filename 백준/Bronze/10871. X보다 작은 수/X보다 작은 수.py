def main():
    _, num = map(int, input().split())
    nums = list(map(int, input().split()))

    result = filter(lambda x: x < num, nums)
    for res in result:
        print(res, end=' ')

if __name__ == "__main__":
    main()