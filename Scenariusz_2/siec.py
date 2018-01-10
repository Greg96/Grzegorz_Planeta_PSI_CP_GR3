from pybrain3 import FeedForwardNetwork, LinearLayer, SigmoidLayer, BiasUnit, FullConnection, RecurrentNetwork, \
    TanhLayer

#network = RecurrentNetwork()  # nowa siec
network=FeedForwardNetwork();

inLayer = LinearLayer(35)  # warstwa wejsciowa
#hiddenLayer = SigmoidLayer(5)  # tworze ukryta warstwe
hiddenLayer=TanhLayer(5);
outLayer = LinearLayer(1)  # tworze warstwe wyjsciowa
bias = BiasUnit()  # inicjalizuje Bias

network.addInputModule(inLayer)
network.addModule(bias)
network.addModule(hiddenLayer)
network.addOutputModule(outLayer)

bias_to_hidden = FullConnection(bias, hiddenLayer)  # lacze warstwy
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

network.addConnection(bias_to_hidden)  # dodaje polaczenie do sieci
network.addConnection(in_to_hidden)
network.addConnection(hidden_to_out)

network.sortModules()
