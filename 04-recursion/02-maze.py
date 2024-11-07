class Maze:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.maze = self._init_maze(self.row, self.col)
        self.start = (1, 1)
        self.end = (row - 2, col - 2)

    def _init_maze(self, row, col):
        "1表示墙，不能移动；0表示可以移动的"
        maze = []
        for i in range(row):
            if i == 0 or i == row - 1:
                maze.append([1 for j in range(col)])
            else:
                maze.append([1 if j == 0 or j == col - 1 else 0 for j in range(col)])
        if row > 4 and col > 4:
            maze[3][1] = 1
            maze[3][2] = 1
            # maze[1][2] = 1
            maze[2][2] = 1
        return maze

    def print_maze(self):
        for row in self.maze:
            for item in row:
                print(item, end=' ')
            print('\t')
        print('\n')

    def find_path(self, i, j):
        if self.maze[self.end[0]][self.end[1]] == 2:
            return True
        else:
            if self.maze[i][j] == 0:
                """策略：下右上左"""
                self.maze[i][j] = 2
                if self.find_path(i + 1, j):
                    return True
                elif self.find_path(i, j + 1):
                    return True
                elif self.find_path(i - 1, j):
                    return True
                elif self.find_path(i, j - 1):
                    return True
                else:
                    """说明这个点是走不通的"""
                    self.maze[i][j] = 3
                    return False
            else:
                """1表示墙，2表示走过了，3表示思路"""
                return False

    def run(self):
        self.find_path(self.start[0], self.start[1])
        self.print_maze()


if __name__ == '__main__':
    maze = Maze(8, 7)
    # maze.print_maze()
    maze.run()
