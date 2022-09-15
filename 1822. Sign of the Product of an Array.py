class Solution(object):
    def signFunc(self, num):
        if num < 0:
            return -1
        elif num > 0:
            return 1
        else:
            return 0
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for x in nums:
            product = product * x
        return self.signFunc(product)
