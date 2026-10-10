class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0

        d={}

        max_subs=0

        while j< len(s):
            d[s[j]]=d.get(s[j],0)+1

            while (j-i+1)-(max(d.values()))>k:
                d[s[i]]-=1

                if d[s[i]]==0:
                    del d[s[i]]

                i+=1

            max_subs=max(max_subs,j-i+1)
            j+=1

        return max_subs