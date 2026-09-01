class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        else:
            s2=sorted(s)
            t2=sorted(t)

            if s2==t2:
                return True

        return False