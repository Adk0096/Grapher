class Graph:

    '''
    MEMBERS :
      | numberOfNodes  :  Number of nodes in the graph.
      | connections{}    :  A Dictionary to store all the connections of a node

    METHODS :
      | __init__(no. of nodes)              :  Initiates the graph.
      |
      | addEdge (from, to, defualt weight ) :  Adds edge between _from
      |                                        and _to with given weight.
      | pathFinder(source)                  :  Finds shortest distance between
                                               source and all other nodes.
    STRUCTURE OF CONNECTIONS :
      | The 'connections' member is a dictionary which will contain the edges
      | as shown :
      |    connections = { Node1 : [  [Connected To , Edge weight],
      |                               [Connected To , Edge weight].....] ,
      |                             ... Similarly other nodes }
      |

    Note : All lists and dictionaries in this class follow 1-based Indices.
    '''

################################################################################
    def __init__(self,no_Of_Nodes):

        '''Initiate the graph object with the number of nodes in it, and
        initialte their connections.'''

        self.numberOfNodes = no_Of_Nodes
        self.connections = {}

################################################################################
    def addEdge(self, _from, _to, weight = 1):

        '''
        Add an edge between _from and _to with/without
        a weight.Default Weight is 1.
        ''''

        if(_from not in self.connections):
            self.connections[_from] = [[ _to   , weight]]
        else:
            self.connections[_from].append([ _to , weight])
        if(_to not in self.connections):
            self.connections[_to] = [[ _from , weight]]
        else:
            self.connections[_to].append([ _from, weight])

################################################################################

    def PathFinder(self, source,):

        '''
            Find the shortest distances between the source and all the
            other nodes in the graph . Return the distances and the respective
            paths . Based on the beautiful Dijkstra's Algorithm .
            Parameters :
                | source : Source Node
        '''

        # dist    : Store the distance from source to other nodes.
        # visited : List which nodes have been visited.
        # path    : List which stores the shortest path to other nodes
        #           from source.

        # Initiate the various lists.
        dist = [-1 for i in range(1+self.numberOfNodes)]
        visited = [-1 for i in range(1+self.numberOfNodes)]
        path = [[] for i in range(1+self.numberOfNodes)]
        NodeQueue = []

        dist[source] = 0
        NodeQueue.append(source)

        # Start Path Finder!
        while(NodeQueue != []):

            # Explore all the neighbours of NodeQueue[head]
            for i in self.connections[NodeQueue[0]]:

                # i represents [ Node Connected to Source , Edge Weight ]
                if( (dist[i[0]] < 0)   or  ((dist[NodeQueue[0]] + i[1]) < dist[i[0]]) ):

                    # Update the dist
                    dist[i[0]] = dist[NodeQueue[0]] + i[1]

                    # Update the path
                    path[i[0]] = list(path[NodeQueue[0]])
                    path[i[0]].append(NodeQueue[0])

                    # Add it to node Queue
                    if(visited[i[0]] != 1 and (i[0] not in NodeQueue)):
                        NodeQueue.append(i[0])

            # After exploring all the neighbours mark it as visited and
            # remove it from the NodeQueue
            visited[NodeQueue[0]] = 1
            NodeQueue.remove(NodeQueue[0])


        # Return the Distances and paths
        return dist[1:],path[1:]

##############################################################################################################
