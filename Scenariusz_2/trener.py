from pybrain3.supervised.trainers.backprop import BackpropTrainer
from pybrain3.tools.validation import Validator

import dane
import siec

trener=BackpropTrainer(siec.network,dane.daneWejsciowe,learningrate=0.5,verbose=True)

trener.trainEpochs(150)

testInput= dane.daneWejsciowe['input']
testTarget= dane.daneWejsciowe['target']

errorComparator=0.900
print("Ilosc trenowanych znakow:",len(dane.daneWejsciowe))
litery=["A","B","C","D","E","F","G","H","I","J","a","b","c","d","e","f","g","h","i","j"]

MSE=0

for i in range(20):
    tmp=siec.network.activate(testInput[i])
    print("dla litery",litery[i],"precyzja wynosi:",tmp[0])
    print("MSE:",Validator.MSE(siec.network.activate(testInput[i]),testTarget[i]))
    MSE+=Validator.MSE(siec.network.activate(testInput[i]),testTarget[i])
    if errorComparator<tmp:
        print("litera:",litery[i],"to DUZA litera")
    else:
        print("litera:",litery[i],"TO mala LITERA")

    print("MSE:",(MSE/20))
