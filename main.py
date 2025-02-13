from src.grid import Grid
from src.graph import Graph

def main():

    # TODO: get input grid and warehouses from external file
    input_grid = [
        ["1", "1", "#", "#", "#", "2"],
        ["1", "1", "#", "#", "#", "2"],
        ["*", "*", "*", "#", "#", "#"],
        ["#", "#", "#", "#", "*", "#"],
        ["#", "#", "*", "*", "3", "3"],
        ["*", "*", "*", "3", "3", "3"]
    ]

    warehouses = [1, 3]

    grid = Grid(input_grid)
    graph = Graph(grid, warehouses)
    graph.to_graphviz()


if __name__ == "__main__":
    main()
