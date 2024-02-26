from collections import deque
from typing import List
# Write any import statements here


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    que = deque()
    uni = set()
    count = 0
    for i in D:
        if i not in uni:
            if len(uni) == K:
                uni.remove(que.popleft())
            uni.add(i)
            que.append(i)
            count += 1

    return count

if __name__ == '__main__':
    print(getMaximumEatenDishCount(6, [1, 2, 1, 2, 1, 2, 1], 2))

