def createMatrix(n):
    m=[]
    for i in range(n):
        c=[]
        for j in range(n):
            c.append(0)
        m.append(c)
    return m
    
def printMatrix(m):
    for i in range(len(m)):
        print(m[i])

print()

f=open("udgraph.txt","r")
line=f.readline()
l=line.split()
n=int(l[0])
m=int(l[1])


adj_matrix=createMatrix(n)
printMatrix(adj_matrix)

print()

for i in range(m):
    line1=f.readline()
    u=int(line1.split()[0])
    v=int(line1.split()[1])
    adj_matrix[u][v]=1
    adj_matrix[u][v]=1
printMatrix(adj_matrix)

import queue
def bfs(G,S):
    q=queue.Queue()
    visited=[0]*n
    print(visited)
bfs(matrix,0,n)
