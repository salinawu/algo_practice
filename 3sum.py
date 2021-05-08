class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        
        nums.sort()
        
        for index, i in enumerate(nums):
            if index > 0 and i == nums[index-1]: # already seen
                continue
            target = nums[index]*-1
            
            twoSumList = self.twoSum(nums[index+1:], target)
            # print("twoSumList: ", twoSumList)
            finalList += [[x[0], x[1], i] for x in twoSumList]
            
        return finalList
        
        
    def twoSum(self, nums: List[int], target: int):
        finalList = set()
        dict = {}
        
        for i in nums:
            if i in dict: 
                finalList.add((i, dict[i]))
            else:
                dict[target - i] = i
                
        return list(finalList)