def getMinProblemCount(N, S) -> int:
    # Write your code here
    found_2, found_1 = False, False
    rem_2, rem_1 = False, False
    max_divi_3 = 0
    for i in S:
        mod = i % 3
        if mod == 1:
            if i == 1:
                found_1 = True
            elif not found_1:
                rem_1 = True
        if mod == 2:
            if i == 2:
                found_2 = True
            elif not found_2:
                rem_2 = True

        max_divi_3 = max(max_divi_3, i // 3)

    if found_1:
        max_divi_3 += 1
    if found_2:
        max_divi_3 += 1

    if not rem_1 and not rem_2:
        return max_divi_3

    return max_divi_3 + 1

if __name__ == '__main__':
    print(getMinProblemCount(5, [1,2,3,4,5]))