from statsmodels.tsa.ar_model import AR
#1 ere colonne
import pandas as pd
la = pd.read_csv('latences.csv',index_col=0 )
latence= la.values[:,0]
latencecloud= la.values[:,1]
train =latence[0:8] # 31 data as train data
test = latence[9:]  # 20 data as test data
trainlist = train.tolist()
testlist = test.tolist()
dataset=trainlist+testlist


i=len(dataset)-len(testlist)
#print(i)
predictions=[]
predict=list()
while(i < len(dataset)): 
  model_ar = AR(trainlist)
  model_ar_fit = model_ar.fit()
  predict = model_ar_fit.predict(end =i)
  predict= predict.tolist()
  #print(predict[-1],i)
  predictions.append(predict[-1])
  i += 1
print("La valeur prédite de latence pour Raspberry Pi 2")
print(predictions[0])
#2 eme colonne
import pandas as pd
la = pd.read_csv('latences.csv',index_col=0 )

latence2= la.values[:,1]
train2 =latence2[0:8] # 31 data as train data
test2 = latence2[9:]  # 20 data as test data
trainlist2 = train2.tolist()
testlist2 = test2.tolist()
dataset2=trainlist2+testlist2

i=len(dataset2)-len(testlist2)
#print(i)
predictions2=[]
predict2=list()
while(i < len(dataset2)): 
  model_ar = AR(trainlist2)
  model_ar_fit = model_ar.fit()
  predict2 = model_ar_fit.predict(end =i)
  predict2= predict2.tolist()
  
  predictions2.append(predict2[-1])
  i += 1
print("La valeur prédite de latence pour RaspberryPi 3")
print(predictions2[0])
print("Raspberry Pi 3 a une valeur prédite de latence plus petite que Raspberry Pi 2")







