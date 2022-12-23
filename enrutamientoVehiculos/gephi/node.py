

class Node_(object):
    def __init__(self) -> None:
        pass


class NodeQuery(Node_):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return "Node Query: " + self.value


class NodeNeigh(Node_):
    def __init__(self, name: str, type: str, rank) -> None:
        self.value = name
        self.type = type
        self.rank = rank

    def __str__(self) -> str:
        return self.value + " " + "ranking: " + str(self.rank)


class NodeSolution(Node_):
    def __init__(self, type) -> None:
        self.type = type

    def __str__(self) -> str:
        return self.type
