class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for k in matrix:
            i=0
            j=len(k)-1

            while i<=j:
                mid=(i+j)//2

                if k[mid]<target:
                    i=mid+1

                elif k[mid]>target:
                    j=mid-1

                else:
                    return True

        return False