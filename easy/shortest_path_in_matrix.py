from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        candidates = {(0, 0)}
        depth = 1
        max_coord = len(grid) - 1
        target = (max_coord, max_coord)


        if grid[target[0]][target[1]] == 1:
            return -1

        if grid[0][0] == 1:
            return -1

        grid[0][0] = 1

        while candidates:
            new_candidates = set()

            for i, j in candidates:
                if (i, j) == target:
                    return depth

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if max_coord >= i + di >= 0 and max_coord >= j + dj >= 0 and grid[i + di][j + dj] == 0:
                            new_candidates |= {(i+di, j+dj)}
                            grid[i + di][j + dj] = 1

            depth += 1
            candidates = new_candidates

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(s.shortestPathBinaryMatrix([
        [0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]))
