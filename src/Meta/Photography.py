from collections import defaultdict
# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int):
    # Write your code here

    dic = defaultdict(list)
    for i, val in enumerate(C):
        if val != '.':
            dic[val].append(i)

    actor_indices = dic['A']
    # print(actor_indices)

    breath = max(X, Y)
    resp = 0

    for ind in actor_indices:
        left_p, right_p = 0,0
        left_b, right_b = 0,0
        for i in range(max(ind - Y, 0), max(ind - X + 1, 0)): # Left of index
            if C[i] == 'P':
                left_p += 1
            if C[i] == 'B':
                left_b += 1
        for i in range(min(ind + X, N), min(ind + Y + 1, N)): # right
            if C[i] == 'P':
                right_p += 1
            if C[i] == 'B':
                right_b += 1
        resp += right_p * left_b + right_b * left_p
    # print (resp)


if __name__ == '__main__':
    getArtisticPhotographCount(8, ".PBAAP.B", 1, 3)