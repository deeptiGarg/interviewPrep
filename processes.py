# Make a process Tree
import numpy as np
#ppid pid name 
processLog = np.array([(28,11,'h'),(0,12,'a'),(0,28,'s'),(12,19,'q'),(11,78,'k'),(78,29,'w'),
(12,56,'n'),(28,77,'r'),(28,111,'m')])

#print(processLog[0])
prHier = {}

for i in range(len(processLog)):
    prHier.setdefault(processLog[i][0],[])
    prHier[processLog[i][0]].append(processLog[i][1])
print(prHier)
