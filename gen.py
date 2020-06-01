import random
import os

def getrands():
    x=random.randint(0,adjSize-1)
    y=random.randint(0,swearSize-1)
    z=random.randint(0,nounSize-1)
    return x,y,z
    
def getIntensifiers():
    intens=[line.rstrip('\n') for line in open("intensifiers.txt")]
    numInt=random.randint(0, 2)
    intList=[]
    for num in range(numInt):
       intList+=[intens[random.randint(0, len(intens)-1 )]]
    return intList
     

def situational():
    x,y,z=getrands()
    print(adj[x].lower(), swear[y], noun[z])

def personal():
    x,y,z=getrands()
    intensifiers=getIntensifiers()
    print("You ", end="")
    for i in intensifiers:
        print(i, end=" ")
    print(adj[x].lower(), swear[y], noun[z])
    
def animal():
    y=random.randint(0,len(singular)-1)
    z=random.randint(0,len(animals)-1)
    intensifiers=getIntensifiers()
    print("You ", end="")
    for i in intensifiers:
        print(i, end=" ")
    print("{}-{}".format(singular[y],animals[z]))

adj=[line.rstrip('\n') for line in open('adj.txt')]
swear=[line.rstrip('\n') for line in open('swear.txt')]
noun=[line.rstrip('\n') for line in open('noun.txt')]
animals=[line.rstrip('\n') for line in open("animals.txt")]
singular=[line.rstrip('\n') for line in open("swear_singular.txt")]
adjSize=len(adj)
swearSize=len(swear)
nounSize=len(noun)
for i in range(5):
    print(i+1, end=": ")
    sel=random.randint(0,2)
    if sel == 0:
        personal()
    elif sel== 1:
        situational()
    else:
        animal()


