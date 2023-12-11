"""
    name:  Will Schmidt
    
    This algorithm is a modified version of this code:
        https://www.geeksforgeeks.org/m-coloring-problem/
    
"""

graph = []

def main():
    global graph

    num_edges = int(input())
    num_vertices = 0

    numToVertex = dict()
    vertexToNum = dict()
    U = list()
    V = list()

    # parse edges into adj
    for _ in range(num_edges):
        u, v = input().split()
        
        # get number for vertices
        if u not in vertexToNum:
            vertexToNum[u] = num_vertices
            numToVertex[num_vertices] = u
            num_vertices += 1
        if v not in vertexToNum:
            vertexToNum[v] = num_vertices
            numToVertex[num_vertices] = v
            num_vertices += 1

        # add vertices to U and V
        U.append(vertexToNum[u])
        V.append(vertexToNum[v])

    graph = [[0]*num_vertices for _ in range(num_vertices)]

    for i in range(len(U)):
        graph[U[i]][V[i]] = 1
        graph[V[i]][U[i]] = 1

    m = 1
    while (not graphColoringAlgorithm(graph, m, num_vertices, numToVertex)):
        m += 1


def printConfiguration(colorArray, num_vertices, num_colors, numToVertex):
    print(num_colors)
    for i in range(num_vertices):
        print(numToVertex[i], colorArray[i] - 1)


def isSafe(v, colorArray, vertex, num_vertices):
    for i in range(num_vertices):
        if graph[v][i] == 1 and colorArray[i] == vertex:
            return False
    return True


def graphColoringAlgorithmUtil(m, colorArray, currentVertex, num_vertices):
    # base case
    if currentVertex == num_vertices:
        return True

    for i in range(1, m + 1):
        if isSafe(currentVertex, colorArray, i, num_vertices) == True:
            colorArray[currentVertex] = i
            if graphColoringAlgorithmUtil(m, colorArray, currentVertex + 1, num_vertices):
                return True

            # backtrack
            colorArray[currentVertex] = 0


def graphColoringAlgorithm(colorArray, m, num_vertices, numToVertex):
    # Initially the color array is initialized with 0.
    colorArray = [0] * num_vertices

    # Call graphColoringAlgorithmUtil() for vertex 0.
    if graphColoringAlgorithmUtil(m, colorArray, 0, num_vertices) == None:
        return False

    # Print the solution
    printConfiguration(colorArray, num_vertices, m, numToVertex)
    return True


if __name__ == "__main__":
    main()
