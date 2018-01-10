from pybrain3.supervised.trainers import BackpropTrainer
from inputLetters import inputDataSet
import inputLetters
import network


letters = ["A", "B", "C", "D", "I", "F", "G", "H", "K", "U", "M", "E", "L", "O", "P", "R", "T", "W", "X", "Y"]
inp = inputDataSet['input']


trainer = BackpropTrainer(network.network, dataset=inputLetters.inputDataSet, learningrate=0.1, verbose=True,
                          momentum=0.01)
trainer.trainEpochs(900)
print("\n\n")

for i in range(20):  # Wydruk
    print("Dla litery", letters[i], "wynik wynosi:")
    temp = network.network.activate(inp[i])
    for k in range(20):
        if temp[k] < 0:
            temp[k] *= (-1)  # poprawa wynikow
    for j in range(20):
        print(temp[j])
print("\n")
