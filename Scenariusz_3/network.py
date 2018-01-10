from pybrain3 import *

network = FeedForwardNetwork()


inLayer = LinearLayer(35)

hiddenLayer = SigmoidLayer(30)

outLayer = LinearLayer(20)

bias = BiasUnit()


network.addInputModule(inLayer)

network.addModule(bias)

network.addModule(hiddenLayer)

network.addOutputModule(outLayer)


bias_to_hidden = FullConnection(bias, hiddenLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)

hidden_to_out = FullConnection(hiddenLayer, outLayer)


network.addConnection(bias_to_hidden)

network.addConnection(in_to_hidden)

network.addConnection(hidden_to_out)


network.sortModules()
