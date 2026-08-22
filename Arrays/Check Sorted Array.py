class Solution:
    def isSorted(self, arr):
        # code here
        for i in range(0, len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True

#TC = O(n)
#SC = O(1)