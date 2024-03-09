# Leetcode 787
import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        queue = collections.deque()
        queue.append((src, 0))

        # make Adj List
        adjList = collections.defaultdict(list)

        for source, destination, cost in flights:
            adjList[source].append((destination, cost))

        cost = [float('inf') for i in range(1 + n)]
        cost[src] = 0

        # print(adjList)
        depth = -1
        while depth < k:
            levelSize = len(queue)
            depth += 1
            for i in range(levelSize):
                top, fare = queue.popleft()
                for des, cos in adjList[top]:
                    cost[des] = min(cost[des], fare + cos)
                    if cost[des] == fare + cos:
                        queue.append((des, cost[des]))

        # print (cost)
        return cost[dst] if cost[dst] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)