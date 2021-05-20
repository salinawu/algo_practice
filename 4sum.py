class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        length = len(nums)
        sols = []
        
        for firstIndex in range(length - 3):
            for secondIndex in range(firstIndex + 1, length - 2):
                thirdIndex = secondIndex + 1
                fourthIndex = length - 1
                while thirdIndex < fourthIndex:
                    sum = nums[firstIndex] + nums[secondIndex] + nums[thirdIndex] + nums[fourthIndex]
                    if sum == target and [nums[firstIndex], nums[secondIndex], nums[thirdIndex], nums[fourthIndex]] not in sols:
                        sols.append([nums[firstIndex], nums[secondIndex], nums[thirdIndex], nums[fourthIndex]])
                        thirdIndex += 1
                    elif sum > target:
                        fourthIndex -= 1
                    else:
                        thirdIndex += 1
                       
        return sols