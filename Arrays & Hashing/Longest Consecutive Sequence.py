from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)< 1):
            return 0
        set_list = list(set(nums))
        longest_list = 0
        candidate = set_list[0]
        while(candidate in set_list):
            long_list = []
            long_list.append(candidate)
            del set_list[set_list.index(candidate)]            
            r = candidate+1
            l = candidate-1
            while(l in set_list):
                long_list.append(l)
                del set_list[set_list.index(l)]
                l-=1
            while(r in set_list):
                long_list.append(r)
                del set_list[set_list.index(r)]
                r+=1
                
            if(len(long_list)>longest_list):
                print(long_list)
                print(longest_list)
                longest_list = len(long_list)
                
            if(len(set_list) > 1):
                candidate = set_list[0]
                
        return longest_list