class Solution6(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

    def convert1(self,s,numRows):

        if numRows == 1 or numRows >= len(s):
            return s
        result = [''] * numRows

        index = 0
        direction = 1 #or -1

        for x in s:
            result[index] += x
            if index == numRows - 1:
                direction = -1
            elif index == 0:
                direction = 1
            index += direction

        return ''.join(result)





testcase = Solution6()
a= testcase.convert1("thebigshort",4)
print(a)

