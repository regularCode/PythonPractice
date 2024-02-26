class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = {}
        letter_keys = []
        digit_logs = {}
        digit_keys = []

        for i, val in enumerate(logs):
            spt = val.split(' ')
            try:
                int(spt[1])
                temp = ' '.join(spt)
                digit_keys.append(temp)
            except ValueError:
                temp = ' '.join(spt[1:])
                if temp in letter_keys:
                    existing = letter_logs[temp]
                    if type(existing) is list:
                        existing.append(spt[0])
                        letter_logs[temp] = existing
                    else:
                        new_list = []
                        new_list.append(existing)
                        new_list.append(spt[0])
                        letter_logs[temp] = new_list
                else:
                    letter_keys.append(temp)
                    letter_logs[temp] = [spt[0]]

        letter_keys.sort()
        res = []
        for i in letter_keys:
            va = letter_logs[i]
            if type(va) is not list:
                res.append(letter_logs[i] + ' ' + i)
            else:
                va.sort()
                for j in list(va):
                    res.append(j + ' ' + i)

        for j in digit_keys:
            res.append(j)

        return res

if __name__ == "__main__":
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    s = Solution()
    print(s.reorderLogFiles(logs))
