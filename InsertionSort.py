# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sol = []
        for i in range(len(pairs)):
            if i == 0:
               sol.append(pairs.copy()) 
               continue
            j = i-1
            tmp = pairs[i]
            while j>=0 and pairs[j].key > tmp.key:
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j-=1
            sol.append(pairs.copy())
        return sol
        
