import string

class Node(object):
    '''
    This is a class that represents a node. The functions of a class are called methods. Instantiations of this class
    will create objects that have access to the methods. 
    
    Each method begins with an argument of "self" which lets the methos know which object it belongs to.
    
    For the Node object, we care about the name of the node and a dictionary naming the adjacent nodes. The adjacent
    dictionary keys will be the name's of adjacent nodes and the value will be the weight of that edge.
    '''
    def __init__(self, name):
        # The init method is magic python method that get's called when an object is instantiated. 
        self.name = name  # Take the name given at instantiation and assign it to the object
        self.adjacent = {}  # When we create the node, we don't know about any adjacent nodes. Create a placeholder
        
    def __str__(self):
        # When printing a node, format it like this:
        return "Node {}: {}".format(self.name, self.adjacent)
    
    def __repr__(self):
        # When representing this object, use the str method
        return self.__str__()

class Graph(object):
    '''
    This class represents a graph. The graph is consists of a collection of nodes. 
    '''
    def __init__(self, adjacency_matrix=None):
        '''
        When the graph is instantiated it will not know about any of its member nodes. There is an optional 
        `adjacency_matrix` argument that defaults to None. If an adjacency_matrix is provided, then we can 
        create the member nodes, their relationships, and add them to this graph.
        '''
        self.nodes = {}
        if adjacency_matrix:
            # We were provided an adjacency matrix
            self._create_member_nodes_from_adjacency_matrix(adjacency_matrix)
            
    def __str__(self):
        return '\n'.join([str(n) for n in self.nodes.values()])
    
    def __repr__(self):
        return self.__str__()
    
    def _create_member_nodes_from_adjacency_matrix(self, adjacency_matrix):
        # A preceeding underscore indicates a method that is only called within the class. 
        # Create nodes and weights from an adjacency matrix (list of lists) and assign them to this graph
        letters = list(string.ascii_lowercase)  # Get a list of letters to assign to the nodes we create
        needed_letters = len(adjacency_matrix)
        if needed_letters > len(letters):
            # Give the user an error that the input matrix is too large to have 
            raise ValueError("The matrix is too large to create from 26 letters. Please manually assign names to nodes and then add them to the graph.")
        
        for i, row in enumerate(adjacency_matrix):  # get an index of the row and the contentx of the row
            letter_name = letters[i]
            node = Node(letter_name)
            for j, column_value in enumerate(row):
                if column_value != 0:  # There is an adjacent node here
                    adjacent_letter_name = letters[j]
                    node.adjacent[adjacent_letter_name] = column_value
            self.nodes[letter_name] = node
            
    def get_distance_of_path(self, path):
        # Given a list of node names within the graph, find its distance using the node adjacency measures
        distance = 0
        for i, node_name in enumerate(path[:-1]):
            # Gets the index and node name for each in the path except for the last one
            this_node = self.nodes[node_name]
            next_node = self.nodes[path[i+1]]
            distance += this_node.adjacent[next_node.name]  # Get the distance from this_node to next node
        
        return distance
    
    def find_all_paths_between(self, a, b, path=None):
        if not path:
            # No path list provided, create one
            path = []

        path = path + [a] # Add a to the path

        if a == b:  # This is a path to itself, at the end of a path
            return [path]
        if a not in self.nodes:  # a could not be found in the graph
            return []
        paths = []
        for node in self.nodes[a].adjacent:  # look to adjacent nodes of a
            if node not in path:
                newpaths = self.find_all_paths_between(node, b, path)  # Recursivly go down another level
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    def shortest_path(self, a, b):
        # Get the distance of each weighted path and return the shortest
        all_paths = self.find_all_paths_between(a, b)
        
        if not all_paths:
            return []
        
        # The shortest path will be the first path in the list
        shortest_path = None
        shortest_distance = None
        
        for path in all_paths:
            p_distance = self.get_distance_of_path(path)
            if not shortest_distance or p_distance < shortest_distance:
                # This path is shorter
                shortest_path = path
                shortest_distance = p_distance
                
        return shortest_path
    
    def is_tree(self):
        # returns True if the graph is a tree, otherwise False
        
        node_names = list(self.nodes.keys())
        first = node_names[0]  # Make sure the first node has a path to all other nodes
        
        for node in node_names:
            if node == first:
                continue  # Don't compare it against itself
            if not self.find_all_paths_between(first, node):
                return False  # No path was found between first and node, this must not be a tree
        
        return True

matrix = [
    [0,23,0,19,0,0,0,0,0,0,0,0],
    [23,0,29,0,1,0,0,0,0,0,0,0],
    [0,29,0,0,0,28,0,0,0,0,0,0],
    [19,0,0,0,9,0,13,0,0,0,0,0],
    [0,1,0,9,0,18,0,25,0,0,0,0],
    [0,0,28,0,18,0,0,0,14,0,0,0],
    [0,0,0,13,0,0,0,2,0,6,0,0],
    [0,0,0,0,25,0,2,0,16,0,20,0],
    [0,0,0,0,0,14,0,16,0,0,0,5],
    [0,0,0,0,0,0,6,0,0,0,8,0],
    [0,0,0,0,0,0,0,20,0,8,0,27],
    [0,0,0,0,0,0,0,0,5,0,27,0]
]
weighted_graph = Graph(matrix)
path = weighted_graph.shortest_path('a', 'l')
distance = weighted_graph.get_distance_of_path(path)

print(f'The shortest path from A -> L is via ', path , ' with a distance of ' , distance)