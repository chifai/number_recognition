class Node:
    def __init__(self):
        self.value = 0.0

class HiddenNode(Node):
    def __init__(self):
        self.weight = 0.5       # initial guess

class OutputNode(Node):
    def __init__(self):
        self.cost = 0.0         # cost = (exp_value - value)^2
        self.exp_value = 0.0    # expected value

class ForwardPropagation:
    def __init__(self):
        pass

class NeuronNetwork:
    def __init__(self, nInputNodeSize, lsHiddenNodeSize, nOutputNodeSize):
        # define input, hidden and output node list
        self.lsInputNode = [Node] * nInputNodeSize
        self.lsHiddenNode = []
        self.lsOutputNode = [OutputNode] * nOutputNodeSize
        nHiddenLayer = len(lsHiddenNodeSize)
        for i in range(nHiddenLayer):
            lsOneHiddenLayer = [HiddenNode] * lsHiddenNodeSize[i]
            self.lsHiddenNode.append(lsOneHiddenLayer)




HNlist = []
HNlist.append(2)
HNlist.append(2)

NN = NeuronNetwork(2, HNlist, 1)
pass