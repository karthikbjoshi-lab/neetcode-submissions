class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i=0
        j=len(nums)-1

        mid=0

        while i<=j:
            mid=(i+j)//2

            if nums[mid]==target:
                return mid

            else:
                if nums[i]<=nums[mid]:
                    if target>=nums[i] and target<nums[mid]:
                        j=mid-1
                    else:
                        i=mid+1

                else:
                    if target<=nums[j] and target>nums[mid]:
                        i=mid+1

                    else:
                        j=mid-1

        
        return -1



