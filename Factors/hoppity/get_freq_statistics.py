import pdb
import json

fsame=open('same_list.json')
samelist=json.load(fsame)
fout=open('res.txt')
ftestname=open('test.txt')
ftrainname=open('train.txt')
flength=open('length.json')

fstatistics_true=open('statistics_true.csv','w')
fstatistics_false=open('statistics_false.csv','w')

program_lengths=json.load(flength)

outlines=fout.readlines()
testnames=ftestname.readlines()
trainnames=ftrainname.readlines()

for i in range(len(trainnames)):
    trainnames[i]=trainnames[i][:-1]
    trainnames[i]=trainnames[i][6:]
for i in range(len(testnames)):
    testnames[i]=testnames[i][:-1]
    testnames[i]=testnames[i][6:]

corrects={}

for l in outlines:
    l=l[:-1]
    name=l.split(' ')[0]
    correct=l.split(' ')[1]
    corrects[name]=correct

#TP=0
#total=len(groundlines)
#for i,groundline in enumerate(groundlines):
for i,testname in enumerate(testnames):
    
    print(i)
    print(testname)
    if not testname in samelist:
        #pdb.set_trace()
        continue
    sames=samelist[testname]
    edit_length=sames[0]
    if edit_length==1:
        continue
    freq=0
    for same in samelist[testname][1]:
        if same in trainnames:
            freq+=1
    #pdb.set_trace()
    program_length=program_lengths[testname]
    #reslines=outlines[i*5:i*5+5]
    #pdb.set_trace()
    if testname in corrects and corrects[testname]=='1':
        fstatistics_true.write(testname+','+str(program_length)+','+str(edit_length)+','+str(freq)+',1\n')
    #if groundline in reslines:
        #fstatistics_true.write(testname+','+str(program_length)+','+str(edit_length)+','+str(freq)+',1\n')
        #print(i)
        #TP+=1
    else:
        fstatistics_false.write(testname+','+str(program_length)+','+str(edit_length)+','+str(freq)+',0\n')
        
        #pdb.set_trace()
#print(TP)
#print(TP/total)
#print(total)


