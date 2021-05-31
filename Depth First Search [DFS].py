# At first you have to make the  adjacency List for the desired graph.I have used a directed graph.
# Use dictionary to represent the adjacency matrix.
Adjacency_List={
    'U':['X','V'],
    'X':['V'],
    'V':['Y'],
    'Y':['X'],
    'W':['Y','Z'],
    'Z':['Z']
}

# Now initialize required variable.
# color--> To point the condition whether a node is traversed already or not or visiting it's adjacency nodes/vertices.
# I have used as follows--> Not_visited--White; Visited completely--Green; visiting running=Red
# Parent--> To point out parent of a node.
# Travel_Time --> To keep track the starting and ending time of traversing a node.
# Traversal_output--> It will show the node sequence of the DFS traversing.
# Time--> It's a global variable to keep the track of time.

Color={}
Parent={}
Travel_Time={}
Traversal_output=[]
Time=0

# initially

for node in Adjacency_List.keys():
    Color[node]= 'White'  # As node is not visited.
    Parent[node]= None
    Travel_Time[node]=[-1,-1] # [Starting_time, Ending_time]=[-1,-1] indicated that the node is not even visited yet.

# DFS algorithm logic is written in the next segment.

def DFS_algo(Source_Node):
    global Time
    Color[Source_Node]='Red'
    Travel_Time[Source_Node][0]= Time   # Starting time = 0
    Traversal_output.append(Source_Node)
    Time=Time+1   # Whenever we change the color we inncrement the time.

    # For the adjacency nodes of the Source_Node
    for adjacency_nodes in Adjacency_List[Source_Node]:
    # Now checking--> is the adjacency node visited or not. If not visited then parent of this node is it's source_node.
        if(Color[adjacency_nodes]== 'White'):
            Parent[adjacency_nodes]=Source_Node
            DFS_algo(adjacency_nodes) # Recursive call to update color, Travel time etc.
# After the completion of checking all the adjacency nodes the Source_Node is now ompletely done.So color will be green.
    Color[Source_Node]='Green'
    Travel_Time[Source_Node][1]=Time
    Time=Time+1

# The following for loop is to provide the Source_Node, when the Scource_Node is not specifically given or \n
# when there exists a node that is separate from from other vertices in the graph.

for item in Adjacency_List.keys():
    if(Color[item]=='White'):
        DFS_algo(item)

print('DFS traversal route is -->', Traversal_output)
print()
print("Starting and Ending time of nodes--->", Travel_Time)
print()
print('Parent of each node-->', Parent)







