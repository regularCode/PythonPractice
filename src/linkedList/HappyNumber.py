# 202
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = []
        sq = [0,1,4,9,16,25,36,49,64,81]

        while n!=1:
            sum = 0
            while n>0:
                rem = n%10
                sum = sum + sq[rem]
                n = n//10
            if sum in dic:
                return False
            dic.append(sum)
            n = sum
        return True