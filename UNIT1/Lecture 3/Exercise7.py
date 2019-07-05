class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        pass
    def getWeight(self):
        # Your code here
        pass
    def __str__(self):
        # Your code here
        pass
Code Editor


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.weight) + ")"

