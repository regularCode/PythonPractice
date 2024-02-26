from collections import defaultdict


def balancedSplitExists(arr):
    # Write your code here
    arr.sort()

    i = 0
    j = len(arr) - 1
    left_sum = right_sum = 0
    split_left = []
    split_right = []

    while i <= j:
        if left_sum < right_sum:
            left_sum += arr[i]
            if arr[i] in split_right:
                return False
            split_left.append(arr[i])
            i += 1
        else:
            right_sum += arr[j]
            if arr[j] in split_left:
                return False
            split_right.append(arr[j])
            j -= 1

    if left_sum == right_sum:
        return True

    return False


def countDistinctTriangles(arr):
  # Write your code here
  uni_tri = []
  count = 0
  for tri in arr:
      l = list(tri)
      l.sort()
      if l not in uni_tri:
          uni_tri.append(l)
          count += 1

  return count

if __name__ == '__main__':
    # print(balancedSplitExists([6,6,7,7,12]))
    print(countDistinctTriangles([[2, 2, 3], [3, 2, 2], [2, 5, 3]]))