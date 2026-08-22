class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = float('-inf')
        second_largest = float('-inf')
        for i in range(0, len(arr)):
            largest = max(arr[i], largest)
        for j in range(0, len(arr)):
            if arr[j]>second_largest and arr[j]<largest:
                second_largest = arr[j]
        if second_largest == float('-inf'):
            return -1
        return second_largest

#TC = O(n)
#SC = O(1)