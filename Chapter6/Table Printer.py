def printTable(l):
    l1=[]
    for i in l:
        m=0
        for j in i:
            if len(j)>m:
                m=len(j)
        l1.append(m+1)  
    for i in range(len(l[0])):
        print(l[0][i].rjust(l1[0])+l[1][i].rjust(l1[1])+l[2][i].rjust(l1[2]))
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
    
