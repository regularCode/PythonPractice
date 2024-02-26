def display(array2D):
    j = 0
    for i in array2D:
        print(j, i)
        j+=1
    print("-----------------\n")


def longestCommonSubsequence(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    display(dp)


def intervalMerge(firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """

    finallist = []
    finallist.extend(firstList)
    finallist.extend(secondList)
    finallist.sort(key= lambda x:x[0])

    output = []
    begin, finish = finallist[0]
    for i in range(1, len(finallist)):
        start, end = finallist[i]
        if begin <= start <= finish:
            finish = max (finish, end)
        elif finish < start:
            output.append([begin, finish])
            begin, finish = start, end

    output.append([begin, finish])

    print(output)


    print (finallist)


def intervalIntersection(firstList, secondList):
    """
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """
    output = []

    n = len(firstList)
    m = len(secondList)
    i,j = 0,0
    while i<n and j<m:
        fs, fe = firstList[i]
        ss, se = secondList[j]

        rs = max(fs, ss)
        re = min(fe, se)

        if rs <= re:
            output.append([rs, re])
            if re == fe:
                i += 1
            else:
                j += 1
        else:
            if fs > se:
                j += 1
            else:
                i += 1

    print(output)

if __name__ == '__main__':
    source = "bbbbab"
    destination = "acbef"
    # longestCommonSubsequence(source, source[::-1])
    # EditDistnace(destination, source)
    intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])



