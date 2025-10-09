#
# THIS SOLUTION IS INCOMPLETE 
#
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start = []
        end = []
        height = []
        currHeight = 0

        n = len(buildings)

        # output should be [[start, height], [start, height]]
        output = []

        for b in buildings:
            start.append(b[0])
            end.append(b[1])
            height.append(b[2])

        i = j = 0

        while i < n and j < n:
            # The next chronological event states that a building will start
            if start[i] < end[j]:
                # The building that is starting has a higher height than the others
                if currHeight < height[i]:
                    currHeight = height[i]
                    output.append([start[i], height[i]])
                i += 1
            else:
                # deal with height
                j += 1
        
        return output
                


        

        
        
