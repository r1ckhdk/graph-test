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
        
    #TODO: get this right
    def get_road_width(self, x: int, y: int) -> int:
        if not self.is_road_cell(x, y):
            return 0

        # checks horizontal width
        horizontal_width = 1
        for dy in [-1, 1]:
            ny = y + dy
            while self.is_inside_grid(x, ny) and self.is_road_cell(x, ny):
                horizontal_width += 1
                ny += dy

        # checks vertical width
        vertical_width = 1
        for dx in [-1, 1]:
            nx = x + dx
            while self.is_inside_grid(nx, y) and self.is_road_cell(nx, y):
                vertical_width += 1
                nx += dx

        return max(horizontal_width, vertical_width)


    #TODO: get this right
    def get_roads(self) -> Roads:
        roads: Roads = []
        visited = set()

        for x in range(self.rows):
            for y in range(self.columns):
                # skips visited or non road cells
                if (x, y) in visited or not self.is_road_cell(x, y):
                    continue

                segment = []
                queue = [(x, y)]  
                width = self.get_road_width(x, y)

                # iterate over road getting all connected cells
                while queue:
                    cx, cy = queue.pop()
                    if (cx, cy) in visited:
                        continue

                    visited.add((cx, cy))
                    segment.append((cx, cy))

                    # checks neighbors
                    for nx, ny in self.get_neighbors(cx, cy):
                        if (nx, ny) not in visited and self.is_road_cell(nx, ny):
                            queue.append((nx, ny))

                # store segment found and its width
                roads.append((segment, width))

        return roads