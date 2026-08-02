class Solution:
    def largest(self, arr):
        # code here
        larger = float("-inf")
        for i in range(0, len(arr)):
            larger = max(arr[i], larger)
        return larger
    
#TC = O(n)
#SC = O(1)