class Node:
    nodeID=""
    nodeAlias=""
    distance = 0
    shortestPathBeforeNode = []
    neighborNodes = []

    def Node(id,alias):
        nodeID=id
        nodeAlias=alias
