import pdb
import json

fsame=open('same_list.json')
samelist=json.load(fsame)

fout=open('pred-test_beam1.txt')
fground=open('tgt-test.txt')
ftestname=open('fname-test.txt')
ftrainname=open('fname-train.txt')
flength=open('length.json')

fstatistics_true=open('statistics_true.csv','w')
fstatistics_false=open('statistics_false.csv','w')

program_lengths=json.load(flength)

outlines=fout.readlines()
groundlines=fground.readlines()
testnames=ftestname.readlines()
trainnames=ftrainname.readlines()

for i in range(len(trainnames)):
    trainnames[i]=trainnames[i][:-1]
for i in range(len(testnames)):
    testnames[i]=testnames[i][:-1]

TP=0
total=len(groundlines)
for i,groundline in enumerate(groundlines):
    
    print(i)
    testname=testnames[i]
    print(testname)
    if not testname in samelist:
        continue
    sames=samelist[testname]
    edit_length=sames[0]
    freq=0
    for same in samelist[testname][1]:
        if same in trainnames:
            freq+=1
    #pdb.set_trace()
    program_length=program_lengths[testname]
    reslines=outlines[i*1:i*1+1]
    if groundline in reslines:
        fstatistics_true.write(testname+','+str(program_length)+','+str(edit_length)+','+str(freq)+',1\n')
        #print(i)
        #TP+=1
    else:
        fstatistics_false.write(testname+','+str(program_length)+','+str(edit_length)+','+str(freq)+',0\n')
        
        #pdb.set_trace()
print(TP)
print(TP/total)
print(total)


