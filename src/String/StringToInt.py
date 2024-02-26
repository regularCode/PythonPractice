class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        add = 0
        for i in s:
            n = ord(i) - 96  # number
            add += self.digit_sum(n)

        for i in range(1, int(k)):
            next_sum = 0
            while add > 0:
                next_sum += self.digit_sum(add % 10)
                add = add // 10
            add = next_sum

        return add
    def digit_sum(self, num):
        add = 0
        while num > 0:
            add += num % 10
            num = num // 10
        return add


if __name__ == "__main__":
    a = input("Enter string ")
    k = input("Enter interation ")
    s = Solution()
    print(s.getLucky(a, k))

