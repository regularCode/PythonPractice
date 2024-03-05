def getSecondsRequired(N, F, P) -> int:
    # Write your code here

    farthest_frog = min(P)
    empty_spaces = N - F - 1 - (farthest_frog - 1)

    return F + empty_spaces

if __name__ == '__main__':
    print(getSecondsRequired(6, 3, [5, 2, 4]))