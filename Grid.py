from .type_aliases import InputGrid, Neighbors, Intersections, Roads, Buildings

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
    
    def get_buildings(self) -> Buildings:
        buildings: Buildings = {}  
        visited = set()

        for x in range(self.rows):
            for y in range(self.columns):
                # skips already visited or non building cells
                if (x, y) in visited or not self.is_building_cell(x, y):
                    continue
                
                building_id = int(self.matrix[x][y])
                queue = [(x, y)]
                building_cells = []

                # gets one cell from queue and adds to building_cells if not already visited
                while queue:
                    cx, cy = queue.pop()
                    if (cx, cy) in visited:
                        continue
                    
                    visited.add((cx, cy))
                    building_cells.append((cx, cy))

                    # checks for neighbors
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = cx + dx, cy + dy
                        if self.is_inside_grid(nx, ny) and (nx, ny) not in visited:
                            if self.is_building_cell(nx, ny) and int(self.matrix[nx][ny]) == building_id:
                                queue.append((nx, ny))

                # storing found buildings and its cells
                if building_id not in buildings:
                    buildings[building_id] = []
                buildings[building_id].extend(building_cells)

        return buildings
        
        
    
    def get_roads(self) -> Roads:
        roads: Roads = []
        visited = set()

        for x in range(self.rows):
            for y in range(self.columns):
                # skips already visited or non road cells
                if (x, y) in visited or not self.is_road_cell(x, y):
                    continue

                # checks for horizontal segments
                if self.is_inside_grid(x, y + 1) and self.is_road_cell(x, y + 1):
                    segment = []
                    while self.is_inside_grid(x, y) and self.is_road_cell(x, y):
                        segment.append((x, y))
                        visited.add((x, y)) 
                        
                        # if its a dead ends, it stops checking
                        if self.is_dead_end(x, y):
                            break
                        
                        y += 1
                    roads.append(segment)
                    continue 

                # does the same for vertical axis
                if self.is_inside_grid(x + 1, y) and self.is_road_cell(x + 1, y):
                    segment = []
                    while self.is_inside_grid(x, y) and self.is_road_cell(x, y):
                        segment.append((x, y))
                        visited.add((x, y))
                        
                        if self.is_dead_end(x, y):
                            break
                        
                        x += 1
                    roads.append(segment)

        return roads