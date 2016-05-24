__author__ = 'aa23314'
class Solution7(object):
    def reverseNum(self, x):
        """
        :type x: int
        :rtype: int
        """

        tempList = [int(y) for y in str(x)]
        length = len(tempList)
        multiplier = [1]*length
        result = 0
        i = 0
        while i < len(tempList):
            if length > 0:
                multiplier[i] = 10**(length - 1)
                result += tempList[length - 1] * multiplier[i]
                i+= 1
                length += -1
        if result > 2**31-1:
            return 0
        else:
            return result

    def reverse(self,x):
        if x >= 0:
            return self.reverseNum(x)
        else:
            x = x * (-1)
            a = self.reverseNum(x)
            return a*(-1)




testcase = Solution7()
a = testcase.reverse(1534236469)
print(a)