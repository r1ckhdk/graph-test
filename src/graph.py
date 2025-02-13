from .grid import Grid
from .type_aliases import Nodes, Edges, Warehouses
from graphviz import Digraph


class Graph:
    def __init__(self, grid: Grid, warehouses: Warehouses):
        self.grid: Grid = grid
        self.warehouses = set(warehouses)
        self.nodes: Nodes = {}
        self.edges: Edges = []
        self.coordinate_to_node = {}

        self.add_buildings()
        self.add_intersections()
        self.add_dead_ends()

    def add_buildings(self) -> None:
        buildings = self.grid.get_buildings()
        for building_id, cells in buildings.items():
            node_id = f"B{building_id}"
            node_type = "warehouse" if building_id in self.warehouses else "building"

            self.nodes[node_id] = {"type": node_type, "cells": cells}

            # maps all building cells to the same node
            for x, y in cells:
                self.coordinate_to_node[(x, y)] = node_id

    def add_intersections(self) -> None:
        intersections = self.grid.get_intersections()
        for idx, (x, y) in enumerate(intersections):
            intersection_id = f"I{idx + 1}"
            self.nodes[intersection_id] = {"type": "intersection", "position": (x, y)}
            self.coordinate_to_node[(x, y)] = intersection_id

    def add_dead_ends(self) -> None:
        dead_end_id = 1
        for x in range(self.grid.rows):
            for y in range(self.grid.columns):
                if self.grid.is_dead_end(x, y):
                    node_id = f"D{dead_end_id}"
                    self.nodes[node_id] = {"type": "dead_end", "position": (x, y)}
                    self.coordinate_to_node[(x, y)] = node_id
                    dead_end_id += 1

    # TODO: function to detect and edges to the graph (roads and its width)

    def to_graphviz(self, output_file: str = "graph", format="png") -> None:
        dot = Digraph("grid", format=format)

        for node_id, node_info in self.nodes.items():
            if node_info["type"] == "building":
                dot.node(node_id, shape="box", label=f"{node_id} (Building)")
            elif node_info["type"] == "warehouse":
                dot.node(node_id, shape="square", label=f"{node_id} (Warehouse)")
            elif node_info["type"] == "intersection":
                dot.node(node_id, shape="circle", label=f"{node_id} (Intersection)")
            elif node_info["type"] == "dead_end":
                dot.node(node_id, shape="diamond", label=f"{node_id} (Dead End)")

        # TODO: when get edges is done, convert them to dot

        dot.save(f"{output_file}.dot")
        dot.render(output_file, format=format, cleanup=True)
        print(dot.source)
