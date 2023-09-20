def ida_star_search(graph, h_costs, start, goal):
    """
        This function performs the (IDA*) algorithm to find
        the minimum-cost path from a start node to a goal node.

        Parameters:
        - graph: A dictionary that represents the graph. Keys are node IDs and values are dictionaries
                 of neighboring nodes and their respective costs to reach from the current node.
        - h_costs: A dictionary that contains the heuristic costs. Keys are node IDs and values are
                   the heuristic costs from that node to the goal.
        - start: The start node ID.
        - goal: The goal node ID.

        Returns:
        - A list that represents the path from the start node to the goal node.
        """

    def dfs(node, g, threshold, path):
        f = g + h_costs.get(node, 0)
        if f > threshold:
            return f, g  # return path/cost

        if node == goal:
            path.append(node)
            return 'FOUND', g

        path.append(node)
        min_f = float('inf')

        for neighbor, cost in graph.get(node, {}).items():
            if neighbor in path:
                continue

            result, new_g = dfs(neighbor, g + cost, threshold, path)  # Unpack returned values

            if result == 'FOUND':
                return 'FOUND', new_g

            if result < float('inf'):
                min_f = min(min_f, result)

        path.pop()
        return min_f, g

    threshold = h_costs.get(start, 0)
    total_cost = 0  # Initialize a variable to keep track of the total cost

    while True:
        print(f"Current threshold: {threshold}")

        path = []
        result, new_cost = dfs(start, 0, threshold, path)  # Unpack returned values

        if result == 'FOUND':
            return new_cost, path  # Return cost and path

        if result == float('inf'):
            return None, None  # Return None for both cost and path

        threshold = result