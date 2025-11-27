class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r= len(numbers)-1
        while(l<r):
            combined_num = numbers[l] + numbers[r]
            if(combined_num == target):
                return [l+1, r+1]
            elif(combined_num > target):
                r-=1
            else:
                l+=1
