"""
1. Input: [11, 2, 5, 9, 10, 3], 12   => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3]       => Output: (11, 9) or None  ex) 11 + 9 = 2 + 5 + 10 + 3
"""
from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    return None



def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    return None


if __name__ == '__main__':
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 11, 3]
    print(get_pair_half_sum(l))
