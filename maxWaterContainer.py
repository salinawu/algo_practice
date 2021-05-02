class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area algo between two points:
        # min(height[a], height[b]) * (b - a)
        
        start_index = 0
        end_index = len(height) - 1
        max_area = 0
        
        while end_index > start_index:
            start_height = height[start_index]
            end_height = height[end_index]
            max_area = max(max_area, min(start_height, end_height) * (end_index - start_index))
            if start_height > end_height:
                end_index -= 1
            else:
                start_index += 1
                
        return max_area
            
        