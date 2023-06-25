class Cell:

    def __init__(self, row, col):
        self.row = row
        self.column = col

    def get_neighbor_count(self, grid):
        rows, columns = len(grid), len(grid[0])
        above = grid[(self.row - 1) % rows][self.column]
        below = grid[(self.row + 1) % rows][self.column]
        left = grid[self.row][(self.column - 1) % columns]
        right = grid[self.row][(self.column + 1) % columns]

        return sum([above, below, left, right])


class Critter(Cell):

    def will_stay_alive(self, grid):
        neighbors = self.get_neighbor_count(grid)
        return 1 if 1 < neighbors < 4 else 0


class Space(Cell):

    def will_be_born(self, grid):
        return 1 if self.get_neighbor_count(grid) == 3 else 0


class Game:

    def __init__(self, grid):
        self.grid = grid

    def iterate(self):
        new_grid = []
        for row_num, row in enumerate(self.grid):
            new_row = []
            for col_num, cell in enumerate(row):
                if cell:
                    cell_obj = Critter(row_num, col_num)
                    new_row.append(cell_obj.will_stay_alive(self.grid))
                else:
                    cell_obj = Space(row_num, col_num)
                    new_row.append(cell_obj.will_be_born(self.grid))
            new_grid.append(new_row)
        self.grid = new_grid