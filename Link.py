import Node
class Link:
    linkId = ""
    sourceNode = Node()
    destinationNode = Node()
    weight = None

    def __init__(id,source,destination,value):
        linkId=id
        sourceNode=source
        destinationNode=destination
        weight = value

