class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    # Function will get start and end, return path
    def get_paths(self, start, end, path=[]):
        # Path is taken as input argument for recursive calls
        path = path + [start]

        # Best case would be, start and end is same
        if start == end:
            return [path]
        
        # No paths present for given start and end
        if start not in self.graph_dict:
            return []
        
        # Regular case, using recursion to fin path
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        if start not in self.graph_dict: # Not a key, not a starting point
            return None
        
        path = path + [start]
        if start == end: # if start and end location is same
            return path
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "New York"
    print(f"Paths between {start} and {end}: ", route_graph.get_shortest_path(start, end))

        