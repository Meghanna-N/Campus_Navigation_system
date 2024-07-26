import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Rectangle

# Define the campus layout as a graph
G = nx.Graph()

# Add nodes with their positions
nodes = {
    'College Gate': (0, 0),
    'Canteen Block': (2, 4),
    'Admin Block': (6, 6),
    'CRC Block': (12,-6),
    'MC Block': (16, 2),
    'Library':(14,-8),
    'Auditorium':(10,-8),
    'Workshop & Mech Lab': (12, 6),
    'Hostel Block': (4, -12),
    'Cricket Ground': (2,-4),
    'Sports Room':(4,-10)

}

for node, position in nodes.items():
    G.add_node(node, pos=position)

# Add edges with weights (distances)
edges = [
    ('College Gate', 'Canteen Block', 1),
    ('Canteen Block', 'Admin Block', 1),
    ('Admin Block', 'Workshop & Mech Lab', 1),
    ('Workshop & Mech Lab', 'MC Block', 1),
    ('MC Block', 'CRC Block', 1),
    ('CRC Block', 'Library', 1),
    ('CRC Block', 'Auditorium', 1),
    ('College Gate','Cricket Ground',2),
    ('Cricket Ground','Sports Room',1),
    ('Sports Room', 'Hostel Block', 1),
    ('College Gate','CRC Block',2),
    ('Cricket Ground','CRC Block',1),
    ('Sports Room','Auditorium',1),
    ('Admin Block','CRC Block',1)
]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Function to draw the campus layout
def draw_campus(G, path=None):
    pos = nx.get_node_attributes(G, 'pos')
    fig, ax = plt.subplots(figsize=(14, 10))

    # Draw nodes as rectangles
    for node, (x, y) in pos.items():
        width = 3.4
        height = 1.5
        ax.add_patch(Rectangle((x - width/2, y - height/2), width, height, edgecolor='black', facecolor='lightGreen'))
        ax.text(x, y, node, ha='center', va='center', fontsize=8)

    # Draw edges
    for edge in G.edges():
        x1, y1 = pos[edge[0]]
        x2, y2 = pos[edge[1]]
        ax.plot([x1, x2], [y1, y2], 'k-')

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    for (n1, n2), weight in edge_labels.items():
        x1, y1 = pos[n1]
        x2, y2 = pos[n2]
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, weight, color='blue', fontsize=10, ha='left')

    # Highlight the path if given
    if path:
        path_edges = list(zip(path, path[1:]))
        for edge in path_edges:
            x1, y1 = pos[edge[0]]
            x2, y2 = pos[edge[1]]
            ax.plot([x1, x2], [y1, y2], 'r-', linewidth=2)

    plt.title("Campus Layout")
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Function to find the shortest path and total distance using Dijkstra's algorithm
def find_shortest_path(G, start, end):
    path = nx.dijkstra_path(G, start, end)
    total_distance = nx.dijkstra_path_length(G, start, end)
    return path, total_distance


# Function to handle user input and call the appropriate functions
def handle_user_input(option):
    if option == '1':
        draw_campus(G)
    elif option == '2':
        start_node = input("Enter the start node: ")
        end_node = input("Enter the end node: ")

        if start_node not in nodes or end_node not in nodes:
            print("Invalid start or end node. Please make sure the nodes exist in the campus layout.")
        else:
            shortest_path, total_distance = find_shortest_path(G, start_node, end_node)
            print("Shortest Path:", shortest_path)
            print("Total Distance Travelled:", total_distance)
            draw_campus(G, shortest_path)
    else:
        print("Invalid option.")


# Main function to present user options
def main():
    while True:
        print("\nCampus Navigation System")
        print("1. Visualize graph")
        print("2. Find shortest path")
        print("3. Exit")

        option = input("Choose an option (1, 2, or 3): ")

        if option == '3':
            print("Exiting the system.")
            break
        else:
            handle_user_input(option)

# Run the main function
if __name__ == "__main__":
    main()