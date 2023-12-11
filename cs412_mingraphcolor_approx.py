"""
    name:  Will Schmidt
    
    This algorithm is a modified version of this code:
        https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
    
    The following code gives an approximate solution by using a greedy algorithm.
"""

def main():
    
    num_edges = int(input())
    adj = list()
    numToVertex = dict()
    vertexToNum = dict()
    counter = 0

    # parse edges into adj
    for _ in range(num_edges):
        a, b = input().split()
        
        # get number for vertices
        if a not in vertexToNum:
            adj.append([])
            vertexToNum[a] = counter
            numToVertex[counter] = a
            counter += 1
        if b not in vertexToNum:
            adj.append([])
            vertexToNum[b] = counter
            numToVertex[counter] = b
            counter += 1

        # add edges to adj
        adj[vertexToNum[a]].append(vertexToNum[b])
        adj[vertexToNum[b]].append(vertexToNum[a])

    min_coloring(adj, counter, numToVertex)


def min_coloring(adj, num_vertices, numToVertex):
    result = [-1] * num_vertices
 
    # Assign the first color to first vertex
    result[0] = 0
 
 
    # A temporary array to store the available colors. 
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * num_vertices
 
    # Assign colors to remaining V-1 vertices
    for u in range(1, num_vertices):
         
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = True
 
        # Find the first available color
        cr = 0
        while cr < num_vertices:
            if (available[cr] == False):
                break
             
            cr += 1
             
        # Assign the found color
        result[u] = cr 
 
        # Reset the values back to false 
        # for the next iteration
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False
 
    # Print the result
    print(max(result) + 1)
    for u in range(num_vertices):
        print(numToVertex[u], result[u])


if __name__ == "__main__":
    main()