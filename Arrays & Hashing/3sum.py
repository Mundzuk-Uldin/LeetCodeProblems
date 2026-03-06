from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums.sort()
        l=0
        r=len(nums)-1
        m=l+1
        threeSumList = []
        while(l<len(sorted_nums)-2):
            sum3 =nums[l]+nums[m]+nums[r]
            if(sum3==0):
                threeSumList.append([nums[l],nums[m],nums[r]])
                l+=1
                r=len(nums)-1
                m=l+1
            elif(sum3>0):
                r-=1
            else:
                m+=1
        return threeSumList