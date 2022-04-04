class Edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v

    def reversed(self):
        return Edge(self.v,self.u)

    def __str__(self):
        return f"{self.u} -> {self.v}"