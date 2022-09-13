class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        array = len(arr)
        subarray = 1
        while subarray <= array:
            for start in range(0,array+1-subarray):
                for end in range(start, start+subarray):
                    ans += arr[end]
            subarray += 2
        return ans
