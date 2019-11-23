class Distances():
    def __init__(self, root) -> None:
        self.root = root
        self.cells = {}
        self.cells[root] = 0


    def __getitem__(self, key): 
        return self.cells[key]

    def __setitem__(self, key, val) -> None:
        self.cells[key] = val
    
    def __contains__(self, key):
        return key in self.cells

    def get_path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]

        while current is not self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break

        return breadcrumbs

    def get_cells(self):
        return self.cells.keys()