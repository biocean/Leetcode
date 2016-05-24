class test(object):
    def plusOne(self, digits): # didnt work
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tempDigits = [0] + digits
        if tempDigits[-1] != 9:
            tempDigits [-1] = tempDigits [-1] + 1
        else:
            self.ninePlusOne(tempDigits,-1)
            i = self.ninePlusOne(tempDigits,-1)
            tempDigits[i] = tempDigits[i] - 1
            
        return tempDigits[1:]
        
    def ninePlusOne(self, x, i):
        length =  -(len(x)-1)
        while i > length:
            x[i] = 0
            i += -1
            if x[i] == 9:
                self.ninePlusOne(x,i)
            else:
                x[i] = x[i] + 1
            return i

class test2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while i>=0:
            digits[i]+=1
            if digits[i]>9:
                digits[i]=0
                i=i-1
                if i<0:
                    digits.insert(0,1)
            else:
                break
        return digits

class test3(object):
    def merge(self, nums1, m, nums2, n):
        indexM, indexN = m - 1, n - 1

        while indexM > -1 and indexN > -1:
            index = indexM + indexN + 1
            if nums1[indexM] > nums2[indexN]:
                nums1[index] = nums1[indexM]
                indexM -= 1
            else:
                nums1[index] = nums2[indexN]
                indexN -= 1

        if indexN > -1:
            nums1[:indexN + 1] = nums2[:indexN + 1]


a = test3()
array1 = [2,3,5,0,0,0,0]
array2 = [1,4]
print(array1[:2])
a.merge(array1,3,array2,2)

print(array1)