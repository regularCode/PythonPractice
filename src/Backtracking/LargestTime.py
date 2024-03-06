
def buildTime(arr):

    h1, h2, m1, m2 = arr

    hours = h1*10 + h2
    mins = m1*10 + m2

    if hours < 24 and mins < 60:
        return hours * 60 + mins

    return 0
def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


def backtrack(arr, start, end):

    if start == end:
        return buildTime(arr)

    maxtime = 0
    for i in range(start, end):
        swap(arr, start, i)
        maxtime = max(backtrack(arr, start + 1, end), maxtime)
        swap(arr, start, i)

    return maxtime


def largestTime(arr):

    return backtrack(arr, 0, len(arr))


if __name__ == '__main__':
    time = largestTime([1, 2, 3, 4])
    print(time)
    print("{:02d}:{:02d}".format(time//60, time %60))
