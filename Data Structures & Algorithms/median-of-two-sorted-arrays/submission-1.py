class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        L = 0
        R = len(nums1)-1

        if len(nums1)%2 == 0:
            return (nums1[(L+R)//2] + nums1[((L+R)//2) + 1]) / 2.0
        else:
            return nums1[(L+R)//2]