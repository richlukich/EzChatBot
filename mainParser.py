import json
import pandas as pd
with open('C:/Users/lukic/AppData/Roaming/JetBrains/PyCharmCE2020.2/scratches/scratch.json', encoding="utf8") as file:
    data=json.load(file)
with open('C:/Users/lukic/AppData/Roaming/JetBrains/PyCharmCE2020.2/scratches/scratch_1.json', encoding="utf8") as file:
    data1=json.load(file)

def makeQ_A(data):
    Q=[]
    A=[]
    for i in range (len(data)):
        Q.append(data[i]['question_text'])
        A.append(data[i]['answer_text'])
    return Q,A
Q_dev,A_dev=makeQ_A(data)
Q_test,A_test=makeQ_A(data1)

dataset_Q_A_dev={'questions':Q_dev,'answers':A_dev}
dataset_Q_A_dev=pd.DataFrame(dataset_Q_A_dev)

dataset_Q_A_dev.to_csv('datasetBotDev.csv')

dataset_Q_A_test={'questions':Q_test,'answers':A_test}
dataset_Q_A_test=pd.DataFrame(dataset_Q_A_test)

dataset_Q_A_test.to_csv('datasetBotTest.csv')