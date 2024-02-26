class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        th = self.intToRomain((num//1000), '', '', 'M')
        h =  self.intToRomain((num%1000)//100, 'M', 'D', 'C')
        t =  self.intToRomain((num%100)//10, 'C', 'L', 'X')
        o =  self.intToRomain((num%10), 'X', 'V', 'I')
        return th + h + t + o



    def intToRomain(self, num, tens, five, ones):
        print (num)
        if num == 0:
            return ''
        if num <= 3:
            return ones*num
        elif num == 4:
            return ones + five
        elif num == 5:
            return five
        elif num == 6:
            return five + ones
        elif num <= 8:
            return five + ones * num
        elif num == 9:
            return five + tens

if __name__ == '__main__':
    s = Solution()

    print (s.intToRoman(3))