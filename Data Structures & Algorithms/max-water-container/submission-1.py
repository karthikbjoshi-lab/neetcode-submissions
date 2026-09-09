class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        width=0
        length=0

        area=1

        i,j=0,len(heights)-1

        while i<j:
            width=j-i
            length=min(heights[i],heights[j])
            
            area=width*length

            max_area=max(max_area,area)

            if heights[i]<heights[j]:
                i+=1

            elif heights[i]>heights[j]:
                j-=1

            else:
                i+=1
                j-=1

        return max_area