from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        largest_sequence = 0
        for n in set_nums:
            large_list = []
            sequence_num = n
            if n-1 not in set_nums:
                while(sequence_num+1 in set_nums):
                    large_list.append(sequence_num)
                    sequence_num += 1
                large_list.append(sequence_num)
            if(largest_sequence < len(large_list)):
                largest_sequence = len(large_list)
        return largest_sequence