class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) < 1:
            return
        for i in range(n):
            nums1[m+i] = nums2[i]
        self.mergeSort(nums1, 0, len(nums1)-1)

    def mergeSort(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s < 1:
            return [arr[s]]
        
        m = (s + e) // 2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m+1, e)

        self._mergeHelper(arr, s, m, e)
        return arr
    
    def _mergeHelper(self, arr: List[int], s: int, m: int, e: int) -> None:
        l=s
        r=m+1
        sort = []
        while l <= m and r <= e:
            if arr[l] <= arr[r]:
                sort.append(arr[l])
                l+=1
            else:
                sort.append(arr[r])
                r+=1
        # Handle leftovers
        while l <= m:
            sort.append(arr[l])
            l+=1
        while r <= e:
            sort.append(arr[r])
            r+=1
        # Replace in-place with original array
        i = s # Original array starting point
        j = 0 # Copy array starting point
        while i <= e:
            arr[i] = sort[j]
            i+=1
            j+=1

