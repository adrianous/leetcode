import heapq
from typing import List

from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        pokers = Counter(hand)
        new_hand = []
        for k, v in pokers.items():
            new_hand.append([k, v])
        new_hand.sort()
        print(new_hand)

        poker_index = 0
        start_num = -1
        pop_num = 0
        while poker_index < len(new_hand) and len(new_hand) > 0:
            if start_num + 1 == new_hand[poker_index][0] or start_num == -1:
                new_hand[poker_index][1] -= 1
                start_num = new_hand[poker_index][0]
            else:
                return False
            if new_hand[poker_index][1] == 0:
                new_hand.pop(poker_index)
                pop_num += 1
            else:
                poker_index += 1
            if poker_index + pop_num == groupSize:
                start_num = -1
                poker_index = 0
                pop_num = 0
        return poker_index == 0


if __name__ == '__main__':
    print(Solution().isNStraightHand([1, 1, 2, 2, 3,3], 3))
