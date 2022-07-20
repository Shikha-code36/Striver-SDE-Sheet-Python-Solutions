'''Leetcode- https://leetcode.com/problems/sort-colors/ '''
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
#Solution1
def sortColors(self, nums):
    for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]> nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
    return nums

#T: O(N^2)
#S: O(1)

#Solution2
def sortColors(self, nums):
        left = cur = 0
        right = len(nums)-1
        while cur<=right:
            if nums[cur]==0:
                nums[left],nums[cur]=nums[cur],nums[left]
                left+=1
                cur+=1
            elif nums[cur]==2:
                nums[cur],nums[right]=nums[right],nums[cur]
                right-=1
            else:
                cur+=1
        return nums
        
#T: O(nlogn)
#S: O(1)

#Solution2
def sortColors(self,nums):
    nums.sort()
    return nums

#T: O(nlogn)
#S: O(1)
