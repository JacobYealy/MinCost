import csv
import heapq


def load_graph(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            from_node, to_node, weight = int(row[0]), int(row[1]), float(row[2])
            if from_node not in graph:
                graph[from_node] = {}
            graph[from_node][to_node] = weight
    return graph


def load_heuristic(file_name):
    heuristics = {}
    min_edge_weights = []

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)

        # Skip header, explanation, and empty rows
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)

        # Read the minEdge values row
        min_edge_weights = list(map(float, next(csv_reader)[1:]))

        # Skip TO row and header
        next(csv_reader)
        next(csv_reader)

        # Reading heuristic values and calculate h based on minEdge values
        for i, row in enumerate(csv_reader):
            from_node = int(row[0])
            heuristics[from_node] = {}

            for j, to_node_cost in enumerate(row[1:], 1):
                if to_node_cost:
                    h = (min_edge_weights[i] + min_edge_weights[j - 1]) / 2
                    heuristics[from_node][j] = h
    return heuristics


def a_star(graph, heuristic, start, goal):
    open_set = [(0, start, [])]  # (cost, current_node, path)
    closed_set = set()

    while open_set:
        cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return cost, path + [current]

        closed_set.add(current)
        for neighbor, edge_cost in graph.get(current, {}).items():
            if neighbor in closed_set:
                continue

            new_cost = cost + edge_cost
            heapq.heappush(open_set, (new_cost + heuristic[current][neighbor], neighbor, path + [current]))


if __name__ == "__main__":
    edge_file = input("Please enter the edge weight file name and extension: ")
    heuristic_file = input("Please enter the heuristic file name and extension: ")
    start_node = int(input("Start node (1 – 200): "))
    end_node = int(input("End Node (1 – 200): "))

    graph = load_graph(edge_file)
    heuristic = load_heuristic(heuristic_file)

    cost, path = a_star(graph, heuristic, start_node, end_node)

    if path:
        print(f"A* minimum cost path\n[{cost}] {' – '.join(map(str, path))}")
    else:
        print("No path exists between the two nodes.")
