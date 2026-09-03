class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        l=[]

        for i in strs:
            sortedS=''.join(sorted(i))
            d[sortedS].append(i)

        return list(d.values())