class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        currSum = float('inf')
        length = len(nums)
        
        for index, lower in enumerate(nums[:-2]):
            middleIndex = index + 1
            upperIndex = length - 1
            
            while middleIndex < upperIndex:
                sum = lower + nums[middleIndex] + nums[upperIndex]
                diff = sum - target
                if abs(diff) < abs(currSum - target):
                    currSum = sum
                if sum > target: 
                    upperIndex -= 1
                else:
                    middleIndex += 1
                    
        return currSum
            
        