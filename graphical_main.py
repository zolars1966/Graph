import pygame as pg
from edge import Edge
from vertex import Vertex
from generic_search import astar, dfs, bfs, Node, node_to_path


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return len(self._edges)

    def add_vertex(self,vertex):
        self._vertixes.append(vertex)
        self._edges.append([])

    def add_edge(self,edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indeces(self,u,v):
        edge = Edge(u,v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indeces(u,v)

    def vertex_at(self,index):
        return self._vertices[index]

    def index_of(self,vertex):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self._vertices.index(vertex))

    def edges_for_index(self, index):
        return self._edges[index]

    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self):
        desc = ""
        for i in range(self.vertex_count):
            print(desc,self.vertex_count,i)
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"

        return desc


if __name__ == "__main__":
        city_graph = Graph((Vertex("Seattle", (9, 7)), 
                            Vertex("San Francisco", (3, 38)),
                            Vertex("Los Angeles", (8, 51)),
                            Vertex("Riverside", (13, 51)),
                            Vertex("Phoenix", (20, 57)),
                            Vertex("Chicago", (65, 33)),
                            Vertex("Boston", (94, 25)),
                            Vertex("New York", (89, 30)),
                            Vertex("Atlanta", (73, 58)),
                            Vertex("Miami", (84, 82)),
                            Vertex("Dallas", (49, 63)),
                            Vertex("Houston", (52, 72)),
                            Vertex("Washington", (85, 37)),
                            Vertex("Detroit", (73, 30)),
                            Vertex("Philadelphia", (87, 34)),
                        ))
        city_graph.add_edge_by_vertices("Seattle", "Chicago")
        city_graph.add_edge_by_vertices("Seattle", "San Francisco")
        city_graph.add_edge_by_vertices("San Francisco", "Riverside")
        city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
        city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
        city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
        city_graph.add_edge_by_vertices("Riverside", "Phoenix")
        city_graph.add_edge_by_vertices("Riverside", "Chicago")
        city_graph.add_edge_by_vertices("Phoenix", "Dallas")
        city_graph.add_edge_by_vertices("Phoenix", "Houston")
        city_graph.add_edge_by_vertices("Dallas", "Chicago")
        city_graph.add_edge_by_vertices("Dallas", "Atlanta")
        city_graph.add_edge_by_vertices("Dallas", "Houston")
        city_graph.add_edge_by_vertices("Houston", "Atlanta")
        city_graph.add_edge_by_vertices("Houston", "Miami")
        city_graph.add_edge_by_vertices("Atlanta", "Chicago")
        city_graph.add_edge_by_vertices("Atlanta", "Washington")
        city_graph.add_edge_by_vertices("Atlanta", "Miami")
        city_graph.add_edge_by_vertices("Miami", "Washington")
        city_graph.add_edge_by_vertices("Chicago", "Detroit")
        city_graph.add_edge_by_vertices("Detroit", "Boston")
        city_graph.add_edge_by_vertices("Detroit", "Washington")
        city_graph.add_edge_by_vertices("Detroit", "New York")
        city_graph.add_edge_by_vertices("Boston", "New York")
        city_graph.add_edge_by_vertices("New York", "Philadelphia")
        city_graph.add_edge_by_vertices("Philadelphia", "Washington")
        print(city_graph)

        bfs_result = bfs("Washington", lambda x: x == "Riverside", city_graph.neighbors_for_vertex)
        
        if bfs_result is None:
            print("no")
        else:
            solution = node_to_path(bfs_result)
            print(solution)

        screen = pg.display.set_mode((1280, 720))
        clock = pg.time.Clock()

        # creating the game logic / environment sample

        upd_ticks = pg.time.get_ticks()

        # main cycle
        while True:
            # surfaces cleaning
            screen.fill((140, 140, 140))
            
            # checking for keyboard, window, mouse inputs or events
            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            for vert in city_graph._vertices:
                pg.draw.circle(screen, "black", vert.pos, 5)

            pg.display.set_caption("$~Graph ~fps: " + str(round(clock.get_fps(), 2)))

            pg.display.flip()
            clock.tick()
