"""
https://www.instagram.com/reel/C00KiZjtPTf/?igsh=ZDE1MWVjZGVmZQ%3D%3D
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        max_area=[]
        
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            max_area.append(area)

            if height[left]>height[right]:
                right-=1
            else:
                left+=1       
        return max(max_area)   
