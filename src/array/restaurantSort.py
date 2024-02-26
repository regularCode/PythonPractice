class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        res = restaurants
        maxPriceFilter = lambda x: (x[3]<=maxPrice)
        maxDistanceFilter = lambda x: (x[4]<=maxDistance)
        veganFriendlyFilter = lambda x: (x[2] == 1)
        res = list(filter(maxDistanceFilter, filter(maxPriceFilter, restaurants)))
        if veganFriendly == 1:
            res = list(filter(veganFriendlyFilter, res))

        func = lambda x: (-x[1], -x[0])
        res.sort(key=func)
        output = []
        for i in res:
            output.append(i[0])
        return output

if __name__ == "__main__":
    logs = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
    s = Solution()
    print(s.filterRestaurants(logs, 1, 20, 10))