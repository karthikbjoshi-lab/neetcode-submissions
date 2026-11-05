class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        i,j=1,max(piles)

        mid=0

        while i<=j:
            time=0

            mid=(i+j)//2

            for k in piles:
                time+=ceil(k/mid)

            if time>h:
                i=mid+1

            else:
                j=mid-1

        return i