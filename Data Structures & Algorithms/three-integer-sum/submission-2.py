class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set()
        l=[]
        nums.sort()

        for idx, k in enumerate(nums):
            if idx>0 and k==nums[idx-1]:
                continue

            i=idx+1
            j=len(nums)-1

            while i<j:
                if nums[i]+nums[j]+k<0:
                    i+=1

                elif nums[i]+nums[j]+k>0:
                    j-=1

                else:
                    l.append([nums[i],nums[j],k])
                    i+=1
                    j-=1

                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1

        return l