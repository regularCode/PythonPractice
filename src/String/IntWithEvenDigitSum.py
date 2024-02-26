class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        unit = self.getUnitDigit(num%10)
        s = ((num % 100) // 10)
        if s > 0:
            return (s-1)*5 + 4 + unit
        else:
            return unit

    def getUnitDigit(self, num):
        if num <= 9 and num % 2 == 1:
            return num // 2
        elif num <= 9 and num % 2 == 0:
            return (num // 2) - 1
