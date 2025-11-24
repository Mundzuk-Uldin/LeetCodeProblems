from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        memo = {}
        for i in range(len(nums)):
            length = self.nextNumInSequence(nums, nums[i], 0, memo)
            if(length > longest_length):
                longest_length = length
                
        return longest_length
        
    def nextNumInSequence(self, nums: List[int], n:int , length: int, memo:dict)-> int:
        if n not in nums:
            return length
        if n in memo:
            return memo[n]
        memo[n] = self.nextNumInSequence(nums,n+1,length, memo)
        return memo[n]