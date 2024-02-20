from typing import List
# reclassification: Medium

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m_arr = []
        total_len = len(nums1) + len(nums2)
        median_i1 = median_i2 = total_len // 2
        median_i2 = median_i1 - 1 if total_len % 2 == 0 else median_i1
        i1 = i2 = 0
        while median_i1 >= len(m_arr):
            if i1 < len(nums1) and (i2 >= len(nums2) or nums1[i1] < nums2[i2]):
                m_arr.append(nums1[i1])
                i1 += 1
            else:
                m_arr.append(nums2[i2])
                i2 += 1
        return (m_arr[median_i1] + m_arr[median_i2]) / 2
