import heapq

def a_star_search(graph, h_costs, start, goal):
    """
        Perform A* search algorithm to find the minimum-cost path from start to goal node.

        Parameters:
        - graph: Dictionary representing the adjacency list of the graph.
                 The keys are nodes and values are dictionaries of neighbors and their costs.
        - h_costs: Dictionary containing heuristic costs for each node to the goal node.
        - start: Start node ID.
        - goal: Goal node ID.

        Returns:
        - Tuple containing the total minimum cost and the list of nodes in the path.
          Returns (None, None) if no path exists.
        """
    open_set = [(0, start, [])]
    closed_set = set()

    while open_set:
        # Pop the node with the smallest f-value from the open set
        cost_so_far, current, path = heapq.heappop(open_set)

        # Skip this node if it has already been visited
        if current in closed_set:
            continue

        path = path + [current]

        if current == goal:
            return cost_so_far, path

        closed_set.add(current)

        # Process all neighbors of the current node
        for neighbor, cost in graph.get(current, {}).items():
            if neighbor in closed_set:
                continue

            # Compute f-value as sum of cost_so_far, edge cost, and heuristic, then add to open set
            heapq.heappush(open_set, (cost_so_far + cost + h_costs.get(neighbor, 0), neighbor, path))

    return None, None
