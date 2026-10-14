class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]

        max_num=float('-inf')

        i,j=0,0

        while j<len(nums):
            max_num=max(max_num,nums[j])

            if j-i+1<k:
                j+=1

            elif j-i+1==k:
                l.append(max_num)
                
                if max_num==nums[i]:
                    i+=1
                    
                    if i<=j:
                        max_num=max(nums[i:j+1])
                    
                    else:
                        max_num=float('-inf')

                else:
                    i+=1
            
                j+=1

        return l    