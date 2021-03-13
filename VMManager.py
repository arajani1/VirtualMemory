import sys
from PhysicalMemory import PhysicalMemory
import numpy as np

initFile = open("init-dp.txt", "r")
inputFile = open("input-dp2.txt", "r")
outputFile = open("output-dp.txt", "w")

index = 0
firstInitLine = "";
secondInitLine = "";
for line in initFile:
    if index == 0:
        firstInitLine = line
        index +=1
    else:
        secondInitLine = line
        
pmI = PhysicalMemory(firstInitLine, secondInitLine)
pm = pmI.PM

pagingDisk = pmI.D

takenFrames = pmI.takenFrames
freeFrameList = []


for i in range(2, 1024):
    if (i not in takenFrames):
        freeFrameList.append(i);
    
def read_block(b, m):
    for i in range(len(pagingDisk[int(b)])):
        pm[m+i] = pagingDisk[int(b)][i]

def getSPW(num):
    binaryStr = ('{0:032b}'.format(num))[5:]
    sStr = binaryStr[0:9]
    pStr = binaryStr[9:18]
    wStr = binaryStr[18:]
    pwStr = binaryStr[9:]
    s = int(sStr,2)
    p = int(pStr,2)
    w = int(wStr,2)
    pw = int(pwStr,2)
    return (s,p,w, pw)
    
# s, p, w, pw = getSPW(1575424)  



virtualAddressLine = ""
for line in inputFile:
    virtualAddressLine = line

VAs = virtualAddressLine.split(" ")

outputStr = ""

for va in VAs:
    s, p, w, pw = getSPW(int(va))
    # print("s: "+str(s)+" p:"+str(p)+" w:"+str(w))
    # print("* "+str(s)+" , "+str(pm[(2*s)+1])+" *")
    if pw >= pm[2*s]:
        outputStr += str(-1)+" "
        continue;
    if pm[(2*s)+1] < 0:
        freeFrame = freeFrameList.pop(0)
        read_block(abs(pm[(2*s)+1]), freeFrame*512)
        pm[(2*s)+1] = freeFrame
        # print(str(freeFrame)+"!")
    if pm[int((pm[(2*s)+1] * 512)+p)] < 0:
        freeFrame = freeFrameList.pop(0)
        b = abs(pm[int((pm[(2*s)+1]*512)+p)])
        read_block(b, freeFrame*512)
        pm[int((pm[(2*s)+1]*512)+p)] = freeFrame
        # print(str(freeFrame)+"!")
    temp = int(pm[(2*s) + 1]*512 + p)
    pa = (pm[temp]*512) + w
    outputStr += str(pa)+" "
    
print(outputStr)

outputFile.write(outputStr[0:len(outputStr)-1]);

outputFile.close()
inputFile.close()
initFile.close()
    
    




# e = None

# for line in inputFile:
