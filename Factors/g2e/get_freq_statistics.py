import json
import pdb

f=open('test_abstract.json')
f2=open('train_abstract.json')
f3=open('statistic_true_3d.csv','w',encoding='ascii')
flength=open('length.json')
program_lengths=json.load(flength)

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


for testobj in testlist:
    if testobj['is_correct']==True: #and len(testobj['tgt_actions'])>2:
        total+=1
        print(iii)
        flag=False
        sameNum=0
        for i in range(len(testobj['tgt_actions'])):
            if testobj['tgt_actions'][i]=="StopEdit":
                testField=""
            else:
                testField=testobj['tgt_actions'][i][testobj['tgt_actions'][i].find("Field("):]
                testField=testField.split(' ')[1]
            testobj['tgt_actions'][i]=testobj['tgt_actions'][i].split('->')[0]
            testobj['tgt_actions'][i]=testobj['tgt_actions'][i].split("'")[0]
            testobj['tgt_actions'][i]+=testField
            #pdb.set_trace()
        for i in range(len(testobj['edits'])):
            if testobj['edits'][i]=="StopEdit":
                testField=""
            else:
                testField=testobj['edits'][i][testobj['edits'][i].find("Field("):]
                testField=testField.split(' ')[1]
            testobj['edits'][i]=testobj['edits'][i].split('->')[0]
            testobj['edits'][i]=testobj['edits'][i].split("'")[0]
            testobj['edits'][i]+=testField
        for trainobj in trainlist:
            if testobj['tgt_actions']==trainobj['tgt_actions'] or testobj['edits']==trainobj['tgt_actions']:
                if flag==False:
                    flag=True
                    iii+=1
                    print(iii)
                    print(testobj['idx'])
                sameNum+=1
                #break
                #print(trainobj['idx'])
        correct='1'
        if testobj['is_correct']==True:
            correct='1'
        else:
            correct='0'
        sameTotal+=sameNum
        lenTotal+=len(testobj['tgt_actions'])
        print(sameNum)
        print(len(testobj['tgt_actions']))
        print(" ")
        program_length=program_lengths[testobj['idx']]
        f3.write(testobj['idx']+","+str(program_length)+","+str(len(testobj['tgt_actions']))+','+str(sameNum)+","+correct+"\n")
                #pdb.set_trace()
                #break
        #if flag==False and len(testobj['tgt_actions'])<50:
        #    iii+=1
        #    print(iii)
        #    print(testobj['idx'])
print(iii)
print(total)
print(sameTotal/total)
print(lenTotal/total)
