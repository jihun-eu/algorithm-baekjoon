import sys
import math
from typing import List, Tuple

input = sys.stdin.readline


def minBought(participants: int, sizeOfParticipants: List[int], tshirts: int, pens: int) -> Tuple[int, int, int]:

    orderTshirts = sum(math.ceil(sizeOfParticipant / tshirts) for sizeOfParticipant in sizeOfParticipants)
    orderBunchOfPens = participants // pens
    orderPens = participants % pens

    return orderTshirts, orderBunchOfPens, orderPens


def main():
    participants = int(input())
    sizeOfParticipants = list(map(int, input().split()))
    tshirts, pens = map(int, input().split())

    orderTshirts, orderBunchOfPens, orderPens = minBought(participants, sizeOfParticipants, tshirts, pens)

    print(orderTshirts)
    print(orderBunchOfPens, orderPens)

if __name__ == "__main__":
    main()