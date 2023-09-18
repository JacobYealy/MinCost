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
        # Calculate the f-value of the current node
        f = g + h_costs.get(node, 0)

        # If the f-value exceeds the current threshold, return f
        if f > threshold:
            return f

        if node == goal:
            path.append(node)
            return 'FOUND'

        # Init the minimum f to infinity
        path.append(node)
        min_f = float('inf')

        # Loop through all neighbors of the current node
        for neighbor, cost in graph.get(node, {}).items():
            if neighbor in path:
                continue

            result = dfs(neighbor, g + cost, threshold, path)

            if result == 'FOUND':
                return 'FOUND'

            if result < float('inf'):
                min_f = min(min_f, result)

        # Pop current node before backtracking
        path.pop()
        return min_f

    threshold = h_costs.get(start, 0)

    while True:
        print(f"Current threshold: {threshold}")

        path = []
        result = dfs(start, 0, threshold, path)

        # If we found the goal node, return the path
        if result == 'FOUND':
            return path

        if result == float('inf'):
            return None

        threshold = result
