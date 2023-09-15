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
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for i, row in enumerate(csv_reader):
            if i < 5:  # Skip the first 5 rows (headers)
                continue
            if not row[0]:  # Skip empty rows or rows with empty "FROM" node
                continue
            try:
                from_node = int(row[0])
            except ValueError:
                continue  # Skip rows that can't be converted to integer
            heuristics[from_node] = {}
            for to_node, h in enumerate(row[1:], 1):
                if h:
                    heuristics[from_node][to_node] = float(h)
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

    return float('inf'), []

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
