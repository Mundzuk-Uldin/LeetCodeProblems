using System;
using System.Collections.Generic;

public class Solution 
{
    public int LongestConsecutive(int[] nums) 
    {
        int longestLength = 0;
        Dictionary<int, int> memo = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Length; i++) 
        {
            int length = NextNumInSequence(nums, nums[i], 0, memo);
            
            if (length > longestLength) 
            {
                longestLength = length;
            }
        }
        
        return longestLength;
    }
    
    private int NextNumInSequence(int[] nums, int n, int length, Dictionary<int, int> memo) 
    {
        if (!nums.Contains(n)) 
        {
            return length;
        }
        if (memo.ContainsKey(n)) 
        {
            return memo[n];
        }
        memo[n] = NextNumInSequence(nums, n + 1, length, memo) + 1;
        return memo[n];
    }
}