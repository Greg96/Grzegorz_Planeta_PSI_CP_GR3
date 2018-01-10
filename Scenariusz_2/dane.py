from pybrain3.datasets.supervised import SupervisedDataSet

daneWejsciowe=SupervisedDataSet(35,1);

#litera A
daneWejsciowe.addSample((0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1),1)
#litera B
daneWejsciowe.addSample((1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0),1)
#Litera C
daneWejsciowe.addSample((0,1,1,1,0,1,0,0,0,1,1,0,0,0, 0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0),1)
#Litera D
daneWejsciowe.addSample((
1 ,1 ,1 ,1 ,0,
1 ,0 ,0 ,0 ,1,
1 ,0 ,0 ,0 ,1,
1 ,0 ,0 ,0 ,1,
1 ,0 ,0 ,0 ,1,
1, 0, 0, 0, 1,
1 ,1 ,1 ,1, 0),1)
#Litera E
daneWejsciowe.addSample((
1 ,1 ,1 ,1 ,1
,1 ,0 ,0, 0 ,0
,1 ,0 ,0 ,0 ,0
,1 ,1 ,1 ,1 ,0
,1 ,0 ,0 ,0 ,0
,1 ,0 ,0 ,0 ,0
,1 ,1 ,1 ,1 ,1),1)
#Litera F
daneWejsciowe.addSample((
1 ,1 ,1 ,1 ,1
,1 ,0 ,0 ,0 ,0
,1 ,0 ,0 ,0 ,0
,1 ,1 ,1 ,1 ,0
,1 ,0 ,0 ,0 ,0
,1 ,0 ,0 ,0 ,0
,1 ,0 ,0 ,0 ,0),1)
#Litera G
daneWejsciowe.addSample((
0 ,1 ,1 ,1 ,0
,1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,0
,1 ,0 ,1 ,1 ,1
,1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1
,0 ,1 ,1 ,1 ,0),1)
#Litera H
daneWejsciowe.addSample((
1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1
,1 ,1 ,1 ,1 ,1
,1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1),1)
#Litera I
daneWejsciowe.addSample((
0 ,1 ,1 ,1 ,0
,0 ,0 ,1 ,0 ,0
,0 ,0 ,1 ,0 ,0
,0 ,0 ,1 ,0 ,0
,0 ,0 ,1 ,0 ,0
,0 ,0 ,1 ,0 ,0
,0 ,1 ,1 ,1 ,0),1)
#Litera J
daneWejsciowe.addSample((
1 ,1 ,1 ,1 ,1
,0 ,0 ,0 ,0 ,1
,0 ,0 ,0 ,0 ,1
,0 ,0 ,0 ,0 ,1
,0 ,0 ,0 ,0 ,1
,1 ,0 ,0 ,0 ,1
,0 ,1 ,1 ,1 ,0),1)
#litera a
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,
0,1,1,1,0,
0,1,0,1,0,
0,1,0,1,0,
0,1,1,1,1),0)
#litera b
daneWejsciowe.addSample((
1,0,0,0,0,
1,0,0,0,0,
1,0,0,0,0,
1,1,1,1,0,
1,0,0,1,0,
1,0,0,1,0,
1,1,1,1,0),0)
#litera c
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,0,0,0,
0,0,0,0,0,
1,1,1,0,0,
1,0,0,0,0,
1,0,0,0,0,
1,1,1,0,0),0)
#litera d
daneWejsciowe.addSample((
0,0,0,0,1,
0,0,0,0,1,
0,0,0,0,1,
0,1,1,0,1,
0,1,0,0,1,
0,1,0,0,1,
0,1,1,1,1),0)
#litera e
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,0,0,0,
1,1,1,0,0,
1,0,0,1,0,
1,1,1,0,0,
1,0,0,0,1,
0,1,1,1,0),0)
#litera f
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,0,1,0,
0,0,1,0,0,
0,1,1,1,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0),0)
#litera g
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,0,0,0,
0,1,1,1,0,
0,1,0,1,0,
0,1,1,1,0,
0,0,0,1,0,
0,1,1,1,0),0)
#litera h
daneWejsciowe.addSample((
1,0,0,0,0,
1,0,0,0,0,
1,0,0,0,0,
1,1,1,1,0,
1,0,0,1,0,
1,0,0,1,0,
1,0,0,1,0),0)
#litera i
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,1,0,0,
0,0,0,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0),0)
#litera j
daneWejsciowe.addSample((
0,0,0,0,0,
0,0,1,0,0,
0,0,0,0,0,
0,0,1,0,0,
0,0,1,0,0,
1,0,1,0,0,
0,1,1,0,0),0)
