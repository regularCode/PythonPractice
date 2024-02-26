def evalRPN(token):
    """
    :type token: List[str]
    :rtype: int
    """
    stack = []
    for i in token:
        print (stack)
        try:
            num = int(i)
            stack.append(num)
        except ValueError:
            top2 = int(stack.pop())
            top1 = int(stack.pop())
            print (top1, i, top2)
            if i == '+':
                stack.append(top1 + top2)
            elif i == '-':
                stack.append(top1 - top2)
            elif i == '*':
                stack.append(top1 * top2)
            elif i == '/':
                if abs(top2) > abs(top1):
                    stack.append(0)
                else:
                    stack.append(int(top1 / top2))
    return stack.pop()


class Solution(object):
    pass


if __name__ == "__main__":
    tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    s = Solution()
    print(evalRPN(tokens))
