class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split("/")
        stack = ['']

        for i in s:
            print (s, stack)
            if i == '..':
                top = stack.pop()
                if top == '':
                    stack.append('')
            elif i == '' or i == '.':
                continue
            else:
                stack.append(i)

        if len(stack) == 1:
            return '/'
        return '/'.join(stack)


if __name__ == "__main__":
    path = "/../"
    s = Solution()
    print(s.simplifyPath(path))