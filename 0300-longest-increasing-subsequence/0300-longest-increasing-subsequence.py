class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []  # tails[i] is the smallest element ending an LIS of length i+1
        
        for num in nums:
            # Binary search to find the first position where tails[i] >= num
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            # If we're at the end, append; otherwise, replace
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        
        return len(tails)