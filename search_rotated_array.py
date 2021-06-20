class Solution:
#     3 - 4 + 1 = 1
#     5 - 4 + 1 = 2
#     0 - 4 + 1 = -3
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        length = len(nums)
        left, right = 0, length - 1
        print("pivot: ", pivot)
        if pivot > 0:
            new_arr = nums[pivot:] + nums[:pivot]
        else:
            new_arr = nums
        print("new arr: ", new_arr)
        while left <= right:
            middle = (right + left) // 2
            if new_arr[middle] == target:
                print("middle: ", middle)
                if pivot > 0:
                    return (middle + pivot) % length
                else:
                    return middle
            elif new_arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
        
    # 6, 7, 8, 1, 2, 3, 4, 5
    # [4,5,6,7,0,1,2]
    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (right + left) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            
            if nums[pivot] <= nums[left]:
                right = pivot
            else:
                left = pivot
        return 0
    