#DNF Algorithm
# Question: https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high = 0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==1:
                mid+=1

            elif nums[mid]==0:
                # Swap nums[mid] with nums[low]
                nums[mid],nums[low] = nums[low],nums[mid]
                # Increase mid and low
                mid+=1
                low+=1

            elif nums[mid]==2:
                # Swap nums[mid] with nums[high]
                nums[mid],nums[high] = nums[high],nums[mid]
                # Decrease high
                high-=1
