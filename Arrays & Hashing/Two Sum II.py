class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        while(l<len(numbers)-1):
            candidate = numbers[l]
            pair = target-candidate
            pair_index = self.binarySearch(numbers, l+1, len(numbers)-1, pair)
            if(pair_index != -1):
                return[l+1, pair_index+1]
            last_element = numbers[l]
            l += 1
            while(numbers[l] == last_element):
                l+=1
        return []  

    def binarySearch(self, arr, low, high, x):
        if high >= low:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid-1, x)
            else:
                return self.binarySearch(arr, mid + 1, high, x)

        else:
            return -1
        