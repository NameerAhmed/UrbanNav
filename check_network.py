import networkx as nx

# Checks if vertiport network is fully connected given restrictions
# This is a simple check and can be expanded to consider factors like no-fly zones, air traffic, etc.
# Definition of connected graph: for every pair of vertices, there is a path connecting them

def check_network(vert: dict, restriction_func: callable) -> nx.Graph|None:
    # Initialize graph with the keys (names) of the vertiports
    network = nx.Graph()
    network.add_nodes_from(vert.keys())

    # Get list of node names to avoid duplicate checks
    nodes = list(vert.keys())
    
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            
            # Pack as (name, coordinates) to match your restriction logic
            v1_data = (u, vert[u])
            v2_data = (v, vert[v])
            
            # Actually CALL the restriction function with arguments
            if not restriction_func(v1_data, v2_data):
                network.add_edge(u, v)

    # Check connectivity
    if nx.is_connected(network):
        print("The network is connected.")
        return network
    else:
        print("The network is not connected.")
        return None

# restriction function example 
# simple example: distance between vertiport is farther than UAV range
def distance_restriction(vertiport1, vertiport2, distance_threshold=5):
    # Distance between vertiport1 and vertiport2 larger than range threshold (e.g., 5 units)
    dist = ((vertiport1[1][0] - vertiport2[1][0])**2 + (vertiport1[1][1] - vertiport2[1][1])**2)**0.5
    return dist > distance_threshold

# Checks if there are any restrictions between two vertiports. This is a placeholder function and can be expanded to include various types of restrictions.    
def restrictions(vertiport1, vertiport2):
    # Example restriction: distance between vertiport1 and vertiport2 is greater than a threshold
    # more complex restrictions can be added here with Boolean logic
    return distance_restriction(vertiport1, vertiport2)

if __name__ == '__main__':

    # Define Vertiport nodes with their coordinates 
    # in real implementation, each vertiport will have more attributes than just coordinates (e.g., capacity, region, etc.)

    vert = {
        'A': (1, 3),
        'B': (3, 5),
        'C': (5, 2),
        'D': (3, 1)
    }

    network = check_network(vert, restrictions)

    if network:
        print("Edges in the network:", network.edges())

    else:
        print("No valid network could be constructed with the given vertiports and restrictions.")
