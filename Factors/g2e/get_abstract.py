import json
import pdb

f=open('test.json',encoding='ascii')
f2=open('test_abstract.json','w',encoding='ascii')

originObjs=json.load(f)

newObjs=[]

for originObj in originObjs:
    idx=originObj['example']['idx']
    tgt_actions=originObj['example']['tgt_actions']
    edits=originObj['hypotheses_logs'][0]['edits']
    is_correct=originObj['hypotheses_logs'][0]['is_correct']
    newobj={}
    newobj['idx']=idx
    newobj['tgt_actions']=tgt_actions
    newobj['edits']=edits
    newobj['is_correct']=is_correct
    newObjs.append(newobj)
    #pdb.set_trace()
json.dump(newObjs,f2)
