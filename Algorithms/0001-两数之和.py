class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        m = len(nums)
        result = []
        for i in range(m - 1):
            for j in range(i + 1, m):
                if nums[i] +nums[j] == target:
                    result.append([i, j])
        return result

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    obj.twoSum(nums, target)
    result = obj.twoSum(nums, target)
    # print(result)    
