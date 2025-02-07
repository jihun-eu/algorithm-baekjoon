import sys

input = sys.stdin.readline


def maximize_value(num, weight, packs):
    dp = [[0] * (num + 1) for _ in range(weight + 1)]

    for i in range(1, num + 1):
        pack_weight, pack_value = packs[i - 1]
        for w in range(1, weight + 1):
            dp[w][i] = dp[w][i - 1]
            if pack_weight <= w:
                dp[w][i] = max(dp[w - pack_weight][i - 1] + pack_value, dp[w][i - 1])

    return dp[-1][-1]


def main():
    num, weight = map(int, input().split())
    packs = [list(map(int, input().split())) for _ in range(num)]

    max_value = maximize_value(num, weight, packs)
    print(max_value)


if __name__ == "__main__":
    main()