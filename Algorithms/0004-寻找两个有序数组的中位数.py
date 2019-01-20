class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort(reverse=False)
        n = len(num)
        median = None
        if n % 2 == 0:
            pos1 = int((n -1 )/ 2)
            median = float((num[pos1] + num[pos1 + 1]) / 2)

        else:
            pos = int((n - 1) / 2)
            median = num[pos]
        return median


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    obj = Solution()
    obj.findMedianSortedArrays(nums1, nums2)
