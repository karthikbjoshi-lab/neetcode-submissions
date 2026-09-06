class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1


        d=dict(sorted(d.items(), key= lambda x: x[1], reverse=True))

        for i in d:
            l.append(i)

        return l[:k]