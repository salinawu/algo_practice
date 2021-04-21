from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        whole_list = []
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                whole_list.extend(nums2[j:])
                break
            elif j >= len(nums2):
                whole_list.extend(nums1[i:])
                break            

            elif nums1[i] < nums2[j]:
                whole_list.append(nums1[i])
                i += 1
            else:
                whole_list.append(nums2[j])
                j += 1


        length = len(whole_list)
        half = floor(length / 2)
        if length % 2 == 0:
            return (whole_list[half] + whole_list[half - 1]) / 2
        else:
            return whole_list[half]
