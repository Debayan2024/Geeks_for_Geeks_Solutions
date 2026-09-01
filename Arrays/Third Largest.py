class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr)<3:
            return -1
        largest = second = third = float('-inf')
        for x in arr:
            if x >= largest:
                third = second
                second = largest
                largest = x
            elif x >= second:
                third = second
                second = x
            elif x >= third:
                third = x
        return third

#TC = O(n)
#SC = O(1)