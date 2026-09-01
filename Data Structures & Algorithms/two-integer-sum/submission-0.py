class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for idx,i in enumerate(nums):
            if target-i not in d:
                d[i]=idx
            else:
                return [d[target-i],idx]
        
                
