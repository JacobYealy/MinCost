import csv
from a_star import a_star_search
from ida_star import ida_star_search

# =============================================================================
# main.py
# Jacob Yealy & Caden Rosenberry
# Artificial Intelligence
#
# Description:
# This program takes an input edge weight file and an input heuristic file
# and then performs the A* minimum path cost finding algorithm.
# =============================================================================

def read_csv_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                from_node, to_node, cost = map(float, row)
                if from_node not in graph:
                    graph[from_node] = {}
                graph[from_node][to_node] = cost
            except ValueError:
                pass
    return graph

def main():
    edge_file = input("Please enter the edge weight file name and extension: ")
    heuristic_file = input("Please enter the heuristic file name and extension: ")

    try:
        graph = read_csv_file(edge_file)
        h_costs = read_csv_file(heuristic_file)
    except FileNotFoundError:
        print("File not found. Exiting.")
        return

    valid_keys = [node for node in graph.keys() if isinstance(node, (int, float))]

    if not valid_keys:
        print("No valid nodes found in the graph. Exiting.")
        return

    min_node = min(int(node) for node in valid_keys)
    max_node = max(int(node) for node in valid_keys)

    start = float(input(f"Start node ({min_node} – {max_node}): "))
    end = float(input(f"End Node ({min_node} – {max_node}): "))

    if start not in graph or end not in graph:
        print("Invalid node ID. Exiting.")
        return

    cost, path = a_star_search(graph, h_costs, start, end)

    if cost is not None:
        print(f"A* minimum cost path\n[{cost}] {' – '.join(map(str, path))}")
    else:
        print("No path exists.")

    path_ida = ida_star_search(graph, h_costs, start, end)
    if path_ida is not None:
        print(f"IDA* path\n{' – '.join(map(str, path_ida))}")
    else:
        print("No path exists in IDA*.")

if __name__ == "__main__":
    main()
