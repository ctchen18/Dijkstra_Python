class Node:
    nodeID=""
    nodeAlias=""
    distance = 0
    shortestPathBeforeNode = []
    neighborNodes = []

    def __init__(self, nid, alias):
        self.nodeID = nid
        self.nodeAlias = alias

    def __hash__(self):
        return hash(str(self.nodeID))

    def __eq__(self, other):
        return str(self.nodeID) == str(other.nodeID)