from src.grid import Grid
from src.graph import Graph

def main():
    input_grid = [
        ["1", "1", "#", "#", "#", "2"],
        ["1", "1", "#", "#", "#", "2"],
        ["*", "*", "*", "#", "#", "#"],
        ["#", "#", "#", "#", "*", "#"],
        ["#", "#", "*", "*", "3", "3"],
        ["*", "*", "*", "3", "3", "3"]
    ]

    warehouses = [1, 3]

    grid = Grid(example_grid)
    graph = Graph(grid, warehouses)


if __name__ == "__main__":
    main()