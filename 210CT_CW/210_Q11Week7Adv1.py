class Vertex:#vertex class
    def __init__(self, vertex):
        self.vertexName = vertex
        self.connections = []

class Graph:#undirected graph class
    def __init__(self):
        self.vertices = {}
        self.adjList = {}
	
    def addVertex(self, vKey):#add new vertex to graph
        self.vertices[vKey.vertexName] = vKey
                  
    def addEdge(self, v1, v2):#add a connection between two elements
        if v1 in self.vertices and v2 in self.vertices:#check if both vertices exist
            self.vertices[v1].connections += [self.vertices[v2]]
            self.vertices[v2].connections += [self.vertices[v1]]

    def listUpdate(self):#updates the graph adjacency list
        for vertex in self.vertices:
            temp = []
            for connection in self.vertices[vertex].connections:
                temp.append(connection.vertexName)
            self.adjList[vertex] = temp

    def listDisplay(self):#displays graph adjacency list
        self.listUpdate()
        for vertex in self.adjList:
            print(vertex, self.adjList[vertex])

    def move(self, vertex, visited):#tries every path possible in the graph starting from a given vertex
        newVisited = visited
        for connection in self.vertices[vertex].connections:
            if connection.vertexName not in visited:
                newVisited += [connection.vertexName]
                newVisited = self.move(connection.vertexName, newVisited)
        return newVisited
        
    def isConnected(self):#check if the graph is connected
        visited = self.move(next(iter(self.vertices)), [next(iter(self.vertices))])
        for vertex in self.vertices:
            if self.vertices[vertex].vertexName not in visited:
                return False
        return True

if __name__ == '__main__':
    v = Vertex(0)
    g = Graph()
    g.addVertex(v)
    g.addVertex(Vertex(1))
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))
    g.addVertex(Vertex(5))
    g.addEdge(0, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(2, 4)
    g.listDisplay()
    print('\n' + str(g.isConnected()))
