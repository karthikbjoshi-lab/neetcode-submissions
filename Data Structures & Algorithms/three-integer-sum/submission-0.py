class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set()
        nums.sort()

        for idx, k in enumerate(nums):
            i,j=idx+1,len(nums)-1

            while i<j:
                if (k+nums[i]+nums[j])<0:
                    i+=1

                elif (k+nums[i]+nums[j])>0:
                    j-=1

                elif k+nums[i]+nums[j]==0:
                    l.add(tuple([nums[i],nums[j],k]))
                    i+=1
                    j-=1

        return list(l)