class memoize:
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


def answer(food, grid):
    leftovers = findSmallestLeftoverFoodForLocation(grid, food, len(grid) - 1, len(grid) - 1)
    return leftovers if leftovers <= food else -1

def findSmallestLeftoverFoodForLocation(grid, foodLeft, i, j):
    @memoize
    def smallest(foodLeft, i, j):
        foodLeft -= grid[i][j]
        if i < 0 or j < 0 or foodLeft < 0:
            return 201 # one more than maximum starting value
        elif i == j == 0:
            return foodLeft
        else:
            return min(smallest(foodLeft, i - 1, j), smallest(foodLeft, i, j - 1))

    return smallest(foodLeft, i, j)