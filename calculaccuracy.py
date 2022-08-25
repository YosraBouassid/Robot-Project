# -*- coding: utf-8 -*-
"""comparaison de 2noeuds edge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Quz93gwhpzDblVugsdO5QxR5jp2g45-Q
"""

#3.6.9 ne marche pas
#il faut version 3.8.2 python
# -*- coding: utf-8 -*

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

import pandas as pd
la = pd.read_csv('mesurenew.csv',index_col=0 )
latence= la.values[:,0]

train =latence[0:31] # 31 data as train data
test = latence[31:]  # 20 data as test data
trainlist = train.tolist()
testlist = test.tolist()
dataset=trainlist+testlist





#******************************
import statistics
# Use: statistics.mean(liste)

from statistics import mean



#  ****************************************************fenetre fixe***************************************************
#_______________calcul de valeurs prédites  de fenetre fixe____________________
i=len(dataset)-len(testlist)
print(i)
predictions=[]
predict=list()
while(i < len(dataset)): 
  model_ar = AR(trainlist)
  model_ar_fit = model_ar.fit()
  predict = model_ar_fit.predict(end =i)
  predict= predict.tolist()
  print(predict[-1],i)
  predictions.append(predict[-1])
  i += 1
print(predictions)  


#***************************fennetre glissante **********************************************************************
#__________________calcul des valeurs predites de fenetre glissante___________
i=len(trainlist)
predict=[]
while(i < len(dataset)): #prédire une seule valeur ou prédire une infinité de valeurs lors du parcours de la voiture
  model_ar = AR(trainlist)
  model_ar_fit = model_ar.fit()
  predict_onevalue = model_ar_fit.predict(end=i)
  predict_onevaluelist= predict_onevalue.tolist()
  predict.append(predict_onevaluelist[-1])
  trainlist.insert(i,dataset[i])
  i += 1
print(predict)





#***************************************fenetre mixte ****************************************************
#fenetre Mixte_______________________________________________________________________________fenetre mixte
#__________________________calcul de predictMixt____________________________________________________________

la = pd.read_csv('mesurenew.csv',index_col=0 )
latence= la.values[:,0]
latencecloud= la.values[:,1]
train =latence[0:31] # 31 data as train data
test = latence[31:]  # 20 data as test data
trainlist = train.tolist()
testlist = test.tolist()
dataset=trainlist+testlist

import numpy as np
i=len(trainlist)
predictmixt=list()
while(i < len(dataset)): 
  model_ar1 = AR(trainlist)
  model_ar_fit = model_ar1.fit()
  predict_onevalue = model_ar_fit.predict(end=i)
  predict_onevaluelist= predict_onevalue.tolist()
  print(predict_onevaluelist[-1],i)
  if(np.asarray(predict_onevaluelist[-1]) not in [np.asarray(dataset[i])- (0.01),np.asarray(dataset[i])+ (0.01)]):
    trainlist.insert(i,dataset[i])
  predictmixt.append(predict_onevaluelist[-1])
  i += 1
print(predictmixt)  

#***********************************Comparaison entre fenetre fixe glissante mixte dans edge node********************************************

#*************************************************************************************************
#*************************************************************************************************
#**************************second noeud*******************second noeud****************************
#*************************************************************************************************
#*************************************************************************************************

#  ****************************************************fenetre fixe***************************************************
import pandas as pd
la = pd.read_csv('mesurenew.csv',index_col=0 )

latence2= la.values[:,1]
train2 =latence2[0:31] # 31 data as train data
test2 = latence2[31:]  # 20 data as test data
trainlist2 = train2.tolist()
testlist2 = test2.tolist()
dataset2=trainlist2+testlist2



#_______________calcul de valeurs prédites  de fenetre fixe____________________
i=len(dataset2)-len(testlist2)
print(i)
predictions2=[]
predict2=list()
while(i < len(dataset2)): 
  model_ar = AR(trainlist2)
  model_ar_fit = model_ar.fit()
  predict2 = model_ar_fit.predict(end =i)
  predict2= predict2.tolist()
  print(predict2[-1],i)
  predictions2.append(predict2[-1])
  i += 1
print(predictions2)  


#***************************fennetre glissante **********************************************************************
#__________________calcul des valeurs predites de fenetre glissante___________
i=len(trainlist2)
predict2=list()
while(i < len(dataset2)): #prédire une seule valeur ou prédire une infinité de valeurs lors du parcours de la voiture
  model_ar = AR(trainlist2)
  model_ar_fit = model_ar.fit()
  predict_onevalue = model_ar_fit.predict(end=i)
  predict_onevaluelist= predict_onevalue.tolist()
  predict2.append(predict_onevaluelist[-1])
  trainlist2.insert(i,dataset2[i])
  i += 1
print(predict2)




#***************************************fenetre mixte ****************************************************
#fenetre Mixte_______________________________________________________________________________fenetre mixte
#__________________________calcul de predictMixt____________________________________________________________

la = pd.read_csv('mesurenew.csv',index_col=0 )
latence= la.values[:,0]
latence2= la.values[:,1]
train2 =latence2[0:31] # 31 data as train data
test2 = latence2[31:]  # 20 data as test data
trainlist2 = train2.tolist()
testlist2 = test2.tolist()
dataset2=trainlist2+testlist2

import numpy as np
i=len(trainlist2)
predictmixt2=list()
while(i < len(dataset2)): 
  model_ar1 = AR(trainlist2)
  model_ar_fit = model_ar1.fit()
  predict_onevalue = model_ar_fit.predict(end=i)
  predict_onevaluelist= predict_onevalue.tolist()
  print(predict_onevaluelist[-1],i)
  if(np.asarray(predict_onevaluelist[-1]) not in [np.asarray(dataset2[i])- (0.01),np.asarray(dataset2[i])+ (0.01)]):
    trainlist2.insert(i,dataset2[i])
  predictmixt2.append(predict_onevaluelist[-1])
  i += 1
print(predictmixt2)  


list1=[1,2,3,4,5,6]
list2=[7,8,9,10]
dat=[1,2,3,4,5,6,7,8,9,10]
pr=[7,55,0,6]
moylist=[]

#liste qui contient les moyennes
for v in range(len(dataset2), 0, -1):
  print(v)
  print( mean(dataset2))
  moylist.append(mean(dataset2))
  sup = dataset2.pop()
del moylist[0]
#liste qui contient les predictions
pre=[]
for v in range(len(predictions2), 0, -1):
  sup = predictions2.pop()
  pre.append(sup)
#liste qui contient test
list2test=[]
for v in range(len(testlist2), 0, -1):
  sup = testlist2.pop()
  list2test.append(sup)

print(moylist)
print(list2test)
print(pre)









tp=0
tn=0
fp=0
fn=0


for mo ,j,i in zip(moylist,list2test,pre):
  if (i < mo and j < mo ):
    tp=tp+1
  if (i > mo and j < mo ):
    fp=fp+1
  if (i < mo and j > mo ):
    fn=fn+1
  if (i > mo and j > mo ):
    tn=tn+1
print(tp , fp ,fn , tn)





