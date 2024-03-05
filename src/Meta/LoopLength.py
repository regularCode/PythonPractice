# Write any import statements here

def getMaxVisitableWebpages(N, L) -> int:
    # Write your code here

    largest = 0

    mem = {}

    for i, val in enumerate(L):
        if val-1 not in mem:
            stack = []
            found_loop = False
            stack.append(i)
            loop = 0
            start = val - 1
            while found_loop:
                loop += 1
                stack.append(start)
                start = L[start] - 1
            print(start)
            # fill mem
            while stack:
                top = stack.pop()
                mem[top] = loop
            print(mem)
        largest = max(loop, largest)

    return 0

if __name__ == '__main__':
    print(getMaxVisitableWebpages(11, [4,1,2,1]))