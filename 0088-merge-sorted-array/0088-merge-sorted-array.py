class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for merged array
        
        # Merge from the end while both arrays have elements
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining nums2 elements if any
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1