import heapq
import networkx as nx


def create_graph():
    # Create road system graph
    G = nx.Graph()
    # A, B, ... - Vertices
    # weight - Edge weight
    edges = [('A', 'B', {'weight': 5}),
             ('A', 'C', {'weight': 7}),
             ('B', 'C', {'weight': 3}),
             ('B', 'D', {'weight': 8}),
             ('C', 'D', {'weight': 6}),
             ('C', 'E', {'weight': 4}),
             ('D', 'E', {'weight': 9}),
             ('D', 'F', {'weight': 2}),
             ('E', 'F', {'weight': 5})]
    G.add_edges_from(edges)
    return G


def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes()}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        if current_node == end:
            break
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = previous_nodes[node]

    return distances[end], path


def main():
    G = create_graph()
    start_node = 'A'
    end_node = 'F'
    distance, path = dijkstra(G, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {path}")
    print(f"Shortest distance from {start_node} to {end_node}: {distance}")


if __name__ == '__main__':
    main()
