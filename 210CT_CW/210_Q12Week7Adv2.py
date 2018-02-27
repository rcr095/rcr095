'''
Implement the structure for a weighted, directed graph G, where nodes consist of positive
integers, then implement an algorithm to find the longest simple path.
'''
class Vertex:#vertex class
    '''
    Title: 210_Q11Week7Adv1
    Author: Rocha, R.
    Date: 2017
    Availability: github.coventry.ac.uk
    '''
    def __init__(self, vertex):
        self.vertexName = vertex
        self.connections = {}

class Graph:#undirected graph class
    '''
    Title: 210_Q11Week7Adv1
    Author: Rocha, R.
    Date: 2017
    Availability: github.coventry.ac.uk
    Function: __init__, addVertex, addEdge, listUpdate, listDisplay, move, isConnected
    '''
    def __init__(self):
        self.vertices = {}
        self.adjList = {}
	
    def addVertex(self, vKey):#add new vertex to graph
        self.vertices[vKey.vertexName] = vKey
                  
    def addEdge(self, v1, v2, weight):#add a connection between two elements
        if v1 in self.vertices and v2 in self.vertices:#check if both vertices exist
            self.vertices[v1].connections[self.vertices[v2]] = [weight]

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

    def weightMove(self, vertex, visited):#tries every possible path stating from a given vertex and returns the longest one
        weight = 0
        vertices = visited
        for connection in self.vertices[vertex].connections:
            if connection.vertexName not in visited:
                tempVisited = visited + [connection.vertexName]
                tempWeight, tempVertices = self.weightMove(connection.vertexName, tempVisited)
                tempWeight = tempWeight + self.vertices[vertex].connections[connection][0]
                if tempWeight > weight:
                    weight = tempWeight
                    vertices = tempVertices
        return weight, vertices
          
    def longPath(self):#tries every path possible and returns the longest one
        weight = 0
        vertices = []
        for vertex in self.vertices:
            tempWeight, tempVertices = self.weightMove(vertex, [vertex])
            if tempWeight > weight:
                weight = tempWeight
                vertices = tempVertices
        return vertices
if __name__ == '__main__':        
    v = Vertex(1)
    g = Graph()
    g.addVertex(v)
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))
    g.addVertex(Vertex(5))
    g.addEdge(1, 2, 1)
    g.addEdge(2, 4, 2)
    g.addEdge(4, 3, 8)
    g.addEdge(4, 5, 1)
    g.addEdge(5, 3, 2)
    g.listDisplay()
    print('\n' + str(g.isConnected()))
    print('\n' + str(g.longPath()))
