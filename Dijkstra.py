from Node import*
class Algorithm:
    nodes = []
    links = []
    mappedNodes = []
    unMappedNodes = []
    previousNodes = {}
    distance = {}

#python is dynamically typed, therefore, variable attributes does not always show in auto-fill
    def __init__(self,nodes,links):
        self.nodes = nodes
        self.links = links

    def executeAlgorithm(self, sourceNode):
        self.distance[sourceNode.nodeID] = 999999
        self.unMappedNodes.add(sourceNode)
        while self.unMappedNodes.count()>0:
            minNode = self.getMinimum(self.unMappedNodes)
            self.mappedNodes.append(minNode)
            self.unMappedNodes.remove(minNode)
            #TODO
    def getMinimum(self,unMappedNodes):
        minNode = None
        for x in range (0,unMappedNodes.count):
            if minNode==None:
                minNode=unMappedNodes[x]
            else:
                if self.getShortestDistance(unMappedNodes[x])>self.getShortestDistance(minNode):
                    minNode = unMappedNodes[x]

        return minNode

    def getShortestDistance(self,destination):
        shortest = self.distance.get(destination)
        if shortest == None:
            return 0.0
        else:
            return shortest

    def findMinimalDistance(self, node):
        neighborNodes = self.getNeighbors(node)

    #def getNeighbors(self,node):
     #   neighbors = []
      #  for link in self.links:
       #     if link.sourceNode == node and not link

x = Node("1","x")

y = Algorithm()
y.executeAlgorithm(x)
z=y.distance.get("1")
print(z.nodeAlias)
