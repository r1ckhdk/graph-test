type Neighbors = list[tuple[int, int]]
type InputGrid = list[list[int | str]]
type Intersections = list[tuple[int, int]]
type Roads = list[list[tuple[int, int]]]
type Buildings = dict[int, list[tuple[int, int]]]
type Nodes = dict[str, dict[str, str]]
type Edges = list[tuple[str, str, int]]
type Warehouses = list[int]
type CoordinateToNode = dict[tuple[int, int], str]
