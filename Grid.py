from .type_aliases import InputGrid, Neighbors, Intersections, Roads

class Grid:
    def __init__(self, input_grid: InputGrid):
        self.matrix: InputGrid = input_grid
        self.rows: int = len(input_grid)
        self.columns: int = len(input_grid[0])
        
        
    def is_building_cell(self, x: int, y: int) -> bool:
        cell = self.matrix[x][y]
        
        # if building ID is str on input, converts it to int
        if isinstance(cell, str) and cell.isdigit():
            cell = int(cell)
            
        return isinstance(cell, int)
    
    def is_road_cell(self, x: int, y: int) -> bool:
        return self.matrix[x][y] == "#"
        
    def is_empty_cell(self, x: int, y: int) -> bool:
        return self.matrix[x][y] == "*"
    
    def is_inside_grid(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.columns
    
    def is_dead_end(self, x: int, y: int) -> bool:
        if not self.is_road_cell(x, y):
            return False

        # if there is only one road neighbor cell, then it is a dead end
        road_neighbors = sum(1 for nx, ny in self.get_neighbors(x, y) if self.is_road_cell(nx, ny))
        return road_neighbors == 1
    
    def get_neighbors(self, x: int, y: int) -> Neighbors:
        neighbors: Neighbors = []
        
        # get neighbors coordinates (up, down, left, right) and checks if they're inside grid
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if self.is_inside_grid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
    
    def get_intersections(self) -> Intersections:
        intersections: Intersections = []
        
        # iterate over grid and get road cells that have 3 or more road neighbors
        for x in range(self.rows):
            for y in range(self.columns):
                if self.is_road_cell(x, y):
                    road_neighbors = sum(1 for nx, ny in self.get_neighbors(x, y) if self.is_road_cell(nx, ny))
                    
                    if road_neighbors >= 3:
                        intersections.append((x, y))
                        
        return intersections
    
    def find_roads(self) -> Roads:
        roads: Roads = []

        # Visitar todas as células
        for x in range(self.rows):
            for y in range(self.columns):
                if self.is_road_cell(x, y):  # Verifica se a célula é uma estrada
                    # Verifica se o segmento horizontal já foi detectado
                    if y + 1 < self.columns and self.is_road_cell(x, y + 1):
                        # Começo do segmento horizontal
                        segment = []
                        while y < self.columns and self.is_road_cell(x, y):
                            segment.append((x, y))
                            y += 1
                        roads.append(segment)

                    # Verifica se o segmento vertical já foi detectado
                    elif x + 1 < self.rows and self.is_road_cell(x + 1, y):
                        # Começo do segmento vertical
                        segment = []
                        while x < self.rows and self.is_road_cell(x, y):
                            segment.append((x, y))
                            x += 1
                        roads.append(segment)
        
        return roads

        
    
    
        
        
    
    