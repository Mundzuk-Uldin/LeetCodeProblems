from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if(s==""):
            return []
        num, leftovers = s.split("#", 1)
        return self.string_divider(int(num), leftovers, list())

        
    def string_divider(self, num: int, leftovers: str, str_list: List[str])-> List[str]:
        if(len(leftovers) <= num):
            return  [leftovers]
        s = leftovers[num:]
        return [leftovers[:num], *self.string_divider(int(s.split("#", 1)[0]),s.split("#", 1)[1], str_list)]
        
        




