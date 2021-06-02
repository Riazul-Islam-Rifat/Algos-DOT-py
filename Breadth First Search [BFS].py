# First import queue as we are going to use this.
import queue
# Now make the adjacency list from the graph.
Adjacency_List = {
    "A":['B','D'],
    "B":['A','C'],
    "C":['B'],
    "D":['A','E','F'],
    "E":['D','F','G'],
    "F":['D','E','H'],
    "G":['E','H'],
    "H":['F','G']
}

# Initializing the variables

Visited = {}  # Keep track whether a node is already visited or not?
Parent = {}  # To represent the parent of a node.
Node_Level = {}  # To keep track the distance of a node from source node.
BFS_Traversal_Sequence= []  # Keep the node sequence of the traversal.
Working_queue = queue.Queue()

# Initial value for all the variables-->

for node in Adjacency_List.keys():
    Visited[node] = False   # False indicates that the node is not visited yet.
    Parent[node] = None     # As the node is not visited at all so the node will have no parents.
    Node_Level[node] = -1   # And taking the node level or distance of the node from the source node is -1.

# Now taking a node as a source node.

Source_node = "A"  # Taking A node as the source node.
Visited[Source_node] = True  # True indicates that the node visited now.
Node_Level[Source_node] = 0   # Distance from source node, here distance is 0 as this node itself is the source node.
Working_queue.put(Source_node)  # Enqueue the node in the working_ queue.


while not Working_queue.empty():
    Dequeued_node = Working_queue.get() # Dequeue the lest most element from the queue.
    BFS_Traversal_Sequence.append(Dequeued_node)  # Popped out node will be added to the traversal route sequentially.
    for Ad_nodes in Adjacency_List[Dequeued_node]:  # Checking for the popped out node's adjacency node.
         if(Visited[Ad_nodes] == False):
             Visited[Ad_nodes] = True
             Parent[Ad_nodes]= Dequeued_node  # As Ad_nodes is derived from dequeued_node.
             Node_Level[Ad_nodes]=Node_Level[Dequeued_node]+1  # As Ad_nodes is derived from dequeued_node.
             Working_queue.put(Ad_nodes)

print('The traversal route for this BFS graph is--->  ',BFS_Traversal_Sequence)
print('Distance from source node---> ', Node_Level)

# Now finding the path of a given vertex(node) from source node.
# I am finding for node "G"

Target_Vertex = "G"
Path = []
while Target_Vertex is not None:  # When Target vertex will have parent.
    Path.append(Target_Vertex)
    Target_Vertex = Parent[Target_Vertex]
Path.reverse()
print("Path from source node to target vertex is  --> ", Path)

# This is for fully connected graph.  RIFAT





