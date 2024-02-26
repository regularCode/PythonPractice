from typing import List
# Write any import statements here


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
    currentLocation = 1
    time = 0
    for num in C:
        time += min(abs(num - currentLocation), abs(N - num + currentLocation))



    return time

if __name__ == '__main__':
    print(getMinCodeEntryTime(3, 3, [1, 2, 3]))