def lastThree(num):
    if num == 0: return ''
    ones_name = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    ten_names = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    ten_ones = num % 100
    hund = num // 100
    resp = ''
    if 19 >= ten_ones > 0:
        resp = ' ' + ones_name[ten_ones]
    else:
        ten = ten_ones // 10
        one = ten_ones % 10
        if one > 0:
            resp = ' ' + ones_name[one]
        if ten > 0:
            resp = ' ' + ten_names[ten] + resp

    if hund > 0:
        resp = ' ' + ones_name[hund] + ' Hundred' + resp

    return resp


def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0: return "Zero"

    thous = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
    i = 0
    resp = ''
    while num > 0:
        last_three = num % 1000
        if last_three > 0:
            resp = lastThree(last_three) + ' ' + thous[i] + resp
        num = num // 1000
        if i == 4:
            i += 1
        i = (i + 1) % 5

    return resp.strip()


class Solution(object):
    pass


if __name__ == '__main__':
    s = Solution()
    print(numberToWords(100000))
