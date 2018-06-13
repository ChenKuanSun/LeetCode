"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sides = 0
        for i in range(len(grid)):
            prev = 0
            for t in grid[i]:
                if t!=prev:
                    prev = t
                    sides+=1
            if grid[i][len(grid[i])-1]==1:
                sides+=1
        
        for i in range(len(grid[0])):
            prev = 0
            for t in range(len(grid)):
                if grid[t][i]!=prev:
                    prev = grid[t][i]
                    sides+=1
            if grid[len(grid)-1][i]==1:
                sides+=1
        
        return sides