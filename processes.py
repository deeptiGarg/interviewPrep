# Make a process Tree
import numpy as np
import json
#ppid pid name 
processLog = np.array([(28,11,'h'),(0,12,'a'),(0,28,'s'),(12,19,'q'),(11,78,'k'),(78,29,'w'),
(12,56,'n'),(28,77,'r'),(28,111,'m')])

prHier = {}   # to store the key =PPID, value = list of children PIDs 
prName = {}   # to store the name of each process; key = PID, value = name

def createTree(nodeID):
    dictJson = {}
    dictJson["PID"] = nodeID
    if(nodeID =='0'):
        dictJson["Name"] = "ROOT"
    else:
        dictJson["Name"] = prName[nodeID]
    if nodeID in prHier:        # If process with ID = nodeID has any children
        dictJson["children"]  = []
        for child in prHier[nodeID]:
            print(child)
            dictJson["children"].append(createTree(child))
    return dictJson

for i in range(len(processLog)):
    prHier.setdefault(processLog[i][0],[])
    prHier[processLog[i][0]].append(processLog[i][1])
    prName[processLog[i][1]] = processLog[i][2]
print(prHier)

jsonData = createTree('0')
with open("tree.json","w") as file:
    json.dump(jsonData,file)

