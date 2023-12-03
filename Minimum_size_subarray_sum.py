"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l = len(nums)
        minimum_length = l + 1
        left, right = 0, 0
        curr_sum = 0

        while right < l:
            curr_sum += nums[right]
            
            while curr_sum >= target:               
                minimum_length = min(minimum_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1            
            right += 1           
        return minimum_length
