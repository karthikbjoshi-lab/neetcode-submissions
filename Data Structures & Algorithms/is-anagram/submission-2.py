class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False

        # else:
        #     s2=sorted(s)
        #     t2=sorted(t)

        #     if s2==t2:
        #         return True

        # return False

        d_s={}
        d_t={}

        for i in s:
            d_s[i]=d_s.get(i,0)+1
        
        for i in t:
            d_t[i]=d_t.get(i,0)+1

        if d_s==d_t:
            return True

        return False