import json
import pdb

f=open('test_abstract.json')
f2=open('train_abstract.json')
f3=open('same_list.json','w')
#f3=open('statisitic_false.csv','w',encoding='ascii')

testlist=json.load(f)
trainlist=json.load(f2)
total=0
iii=0
sameTotal=0
lenTotal=0

for j in range(len(trainlist)):
    trainobj=trainlist[j]
    for i in range(len(trainobj['tgt_actions'])):
        if trainobj['tgt_actions'][i]=="StopEdit":
            trainField=""
        else:
            trainField=trainobj['tgt_actions'][i][trainobj['tgt_actions'][i].find("Field("):]
            try:
                trainField=trainField.split(' ')[1]
            except:
                trainField=""
        trainobj['tgt_actions'][i]=trainobj['tgt_actions'][i].split('->')[0]
        trainobj['tgt_actions'][i]=trainobj['tgt_actions'][i].split("'")[0] 
        trainobj['tgt_actions'][i]+=trainField

for j in range(len(testlist)):
    testobj=testlist[j]
    for i in range(len(testobj['tgt_actions'])):
        if testobj['tgt_actions'][i]=="StopEdit":
            testField=""
        else:
            testField=testobj['tgt_actions'][i][testobj['tgt_actions'][i].find("Field("):]
            try:
                testField=testField.split(' ')[1]
            except:
                testField=""
        testobj['tgt_actions'][i]=testobj['tgt_actions'][i].split('->')[0]
        testobj['tgt_actions'][i]=testobj['tgt_actions'][i].split("'")[0] 
        testobj['tgt_actions'][i]+=testField

fulllist=trainlist
fulllist.extend(testlist)

samelist={}

for testobj in fulllist:
    samelist[testobj['idx']]=[len(testobj['tgt_actions']),[]]
    if 1==1: #and len(testobj['tgt_actions'])>2:
        total+=1
        print(total)
        print(testobj['idx'])
        flag=False
        sameNum=0
        for trainobj in fulllist:
            if testobj['tgt_actions']==trainobj['tgt_actions']:
                samelist[testobj['idx']][1].append(trainobj['idx'])
                #print("    "+trainobj['idx'])
json.dump(samelist,f3,indent=4)
                #break
                #print(trainobj['idx'])
        #sameTotal+=sameNum
        #lenTotal+=len(testobj['tgt_actions'])
        #print(sameNum)
        #print(len(testobj['tgt_actions']))
        #print(" ")
        #f3.write(testobj['idx']+","+str(sameNum)+","+str(len(testobj['tgt_actions']))+","+correct+"\n")
                #pdb.set_trace()
                #break
        #if flag==False and len(testobj['tgt_actions'])<50:
        #    iii+=1
        #    print(iii)
        #    print(testobj['idx'])
#print(iii)
#print(total)
#print(sameTotal/total)
#print(lenTotal/total)
