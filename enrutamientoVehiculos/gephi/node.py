

class Node(object):
    def __init__(self) -> None:
        pass


class NodeQuery(Node):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return "Node Query: " + self.value


class NodeNeigh(Node):
    def __init__(self, name: str, type: str, rank_value: float) -> None:
        self.value = name
        self.type = type
        self.rank_value = rank_value
