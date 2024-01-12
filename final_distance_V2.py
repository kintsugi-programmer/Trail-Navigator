import heapq
import csv
from collections import defaultdict

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def read_edges_from_csv(file_path):
    edges = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            u, v, w = map(int, row)
            edges.append(Edge(u, v, w))
    return edges

def read_node_names_from_csv(file_path):
    node_names = {}
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            node_id, node_name = row
            node_names[int(node_id)] = node_name
    return node_names

def initialize_adjacency_list(edges):
    adj = defaultdict(list)
    for edge in edges:
        add_edge(adj, edge)
    return adj

def validate_node_names(node_names, src_name, dest_name):
    if src_name not in node_names.values() or dest_name not in node_names.values():
        raise ValueError("Invalid node names. Please provide valid node names.")

def print_readable_path(path, node_names):
    print("Shortest Path:", " -> ".join(node_names[node_id] for node_id in path))

if __name__ == "__main__":
    csv_file_path = 'edges.csv'
    node_names_csv_file_path = 'id.csv'

    edges = read_edges_from_csv(csv_file_path)
    node_names = read_node_names_from_csv(node_names_csv_file_path)

    max_node = max(max(edge.u, edge.v) for edge in edges)
    N = max_node + 1
    adj = initialize_adjacency_list(edges)

    src_name = input("Type your Starting State: ")
    dest_name = input("Type your Destination State: ")

    validate_node_names(node_names, src_name, dest_name)

    src = next(key for key, value in node_names.items() if value == src_name)
    dest = next(key for key, value in node_names.items() if value == dest_name)

    distances, path = dijkstra(adj, src, dest)

    print(f"Shortest Distance: {src_name} -> {dest_name} : {distances[dest]}")
    print_readable_path(path, node_names)
