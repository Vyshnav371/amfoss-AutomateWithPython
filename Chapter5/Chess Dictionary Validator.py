def isValidChessBoard(d):
    q=0
    pieces=['bking','wking','bqueen','wqueen','bpawn','wpawn','bknight','wknight',
            'bbishop','wbishop','wrook','brook',]
    countd={}
    letter='abcdefgh'
    number='12345678'
    for i,j in d.items():
        if i[0] not in number or i[1] not in letter:
            q=1
            break
        elif j not in pieces:
            q=1
            break
        else:
            if j not in countd.keys():
                countd[j]=1
            else:
                countd[j]+=1
    for i,j in countd.items():
        if i=='bking' or i=='wking':
            if j>1:
                q=1
                break
        elif i=='bqueen' or i=='wqueen':
            if j>1:
                q=1
                break
        elif i=='bpawn' or i=='wpawn':
            if j>8:
                q=1
                break
        elif i=='bknight' or i=='wknight':
            if j>2:
                q=1
                break
        elif i=='bbishop' or i=='wbishop':
            if j>2:
                q=1
                break
        elif i=='brook' or i=='wrook':
            if j>2:
                q=1
                break
    print(countd)
    if q==0:
        print("TRUE")
    else:
        print("FALSE")
d=eval(input('enter dictionary'))
isValidChessBoard(d)
