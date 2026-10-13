class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_s1={}
        d_s2={}

        i,j=0,0

        n=len(s1)
        for k in s1:
            d_s1[k]=d_s1.get(k,0)+1

        while j<len(s2):
            d_s2[s2[j]]=d_s2.get(s2[j],0)+1

            if j-i+1<len(s1):
                j+=1

            elif j-i+1==len(s1):
                if d_s1==d_s2:
                    return True

                d_s2[s2[i]]-=1

                if d_s2[s2[i]]==0:
                    del d_s2[s2[i]]

                i+=1
                j+=1

        return False

