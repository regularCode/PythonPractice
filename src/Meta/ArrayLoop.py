def longestLoop(arr):
    n = len(arr)

    longest = 0
    dup = set()
    mem = {}

    for i in range(n):
        if i not in dup:
            elements = []
            elements.append(i)
            dup.add(i)
            temp = arr[i]
            loop = 0
            while i != temp and temp not in dup:
                elements.append(temp)
                dup.add(temp)
                temp = arr[temp]
                loop += 1
            print(dup, elements)
            longest = max(longest, loop)

    print("Longest loop length is ", longest)



if __name__ == '__main__':
    longestLoop([1,0,3,4,5,1,1])


