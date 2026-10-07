class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        max_count=0
        d={}

        while j< len(s):
            d[s[j]]=d.get(s[j],0)+1

            while d[s[j]]>1:

                d[s[i]]-=1

                if d[s[i]]==0:
                    del d[s[i]]
 
                i+=1
                
            max_count=max(max_count, j-i+1)

            j+=1

        return max_count