# Write any import statements here
from collections import defaultdict


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    left_p = left_b = 0
    right_p = right_b = 0

    # Create right window
    for i in range(X - 1, Y):
        if C[i] == 'P':
            right_p += 1
        if C[i] == 'B':
            right_b += 1

    cou = 0

    for i, val in enumerate(C):
        # Adjust left window
        if i - Y - 1 >= 0:
            left_p -= 1 if C[i - Y - 1] == 'P' else 0
            left_b -= 1 if C[i - Y - 1] == 'B' else 0
        if i - X >= 0:
            left_p += 1 if C[i - X] == 'P' else 0
            left_b += 1 if C[i - X] == 'B' else 0

        # Adjust right window
        if i + X - 1 < N:
            right_p -= 1 if C[i + X - 1] == 'P' else 0
            right_b -= 1 if C[i + X - 1] == 'B' else 0
        if i + Y < N:
            right_p += 1 if C[i + Y] == 'P' else 0
            right_b += 1 if C[i + Y] == 'B' else 0

        if val == 'A':
            cou += left_p * right_b + left_b * right_p

    return cou

if __name__ == '__main__':
    print (getArtisticPhotographCount(5, "APABA", 1, 2))