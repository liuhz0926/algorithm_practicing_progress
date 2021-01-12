DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if not grid or not grid[0]:
            return None

        n = len(grid)
        m = len(grid[0])

        zombie_queue = collections.deque([])
        human_num = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    human_num += 1
                if grid[i][j] == 1:
                    zombie_queue.append((i, j))

        day = 0
        while zombie_queue:
            increase_zombie = 0
            for _ in range(len(zombie_queue)):
                x, y = zombie_queue.popleft()
                for dx, dy in DIRECTIONS:
                    next_x = x + dx
                    next_y = y + dy
                    if self.is_valid(grid, next_x, next_y):
                        increase_zombie += 1
                        grid[next_x][next_y] = 1
                        zombie_queue.append((next_x,  next_y))
            # 有可能不能在加新的了。周围都是墙
            if increase_zombie == 0:
                break
            human_num -= increase_zombie
            day += 1
            # human 全变成zombie了：
            if human_num == 0:
                break

        if human_num > 0:
            return -1
        return day

    def is_valid(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])

        if not (0 <= x < n and 0 <= y < m):
            return False
        if grid[x][y] != 0:
            return False

        return True