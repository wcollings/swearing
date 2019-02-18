import random
import os

adj=[line.rstrip('\n') for line in open('adj.txt')]
swear=[line.rstrip('\n') for line in open('swear.txt')]
noun=[line.rstrip('\n') for line in open('noun.txt')]
adjSize=len(adj)
swearSize=len(swear)
nounSize=len(noun)
x=random.randint(0,adjSize-1)
y=random.randint(0,swearSize-1)
z=random.randint(0,nounSize-1)

print(adj[x], swear[y], noun[z])
