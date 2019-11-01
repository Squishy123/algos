from fractions import Fraction as frac

#Set the row value
def setRow(mex, rowIndex, value):
    mex[rowIndex]=value

#Return the value of row1 + row2
def addRows(mex, r1, r2, i1, i2):
    print(f"ADDED R{i1} + R{i2}")
    return [r1[i]+r2[i] for i in range(len(r1))]

#Apply and return the row of r*factor
def applyFactor(mex, r, factor):
    print(f"FACTORED R{str(r)}({factor})")
    return [mex[r][i] * factor for i in range(len(mex[r]))]

#Swap rows of row1 and row2
def swapRows(mex, r1, r2):
    print(f"SWAPPED R({str(r1)},{str(r2)})")
    temp=mex[r1]
    mex[r1]=mex[r2]
    mex[r2]=temp

def toRef(mex):
    row=0
    col=0
    while(row < len(mex)):
        print(mex[row][col])
        # if its 0 attempt swap through rows
        if(mex[row][col] == 0):
            foundSwap=False
            for r in range(row, len(mex)):
                if(mex[r][col] != 0):
                    swapRows(mex, r, row)
                    foundSwap=True
                    break
                pretty(mex)

            if(not foundSwap):
                col+=1
        else:
            for r in range(row+1, len(mex)):
                if(mex[row][col] != 0):
                    factor=-1*frac(mex[r][col]/mex[row][col])
                    fRow=applyFactor(mex,row,factor)
                    setRow(mex, r, addRows(mex, fRow,mex[r], row, r))
                pretty(mex)
            row+=1
            col+=1
        
        pretty(mex)
    
    return mex

def pretty(mex):
    pret=""
    for x in range(len(mex)):
        for y in range(len(mex[x])):
            pret+=str(mex[x][y]) + " "
        pret+="\n"
    return pret

#print(pretty(toRef([[1, 3, 4, 5], [2, 6, 5, 3], [3, 6, 7, 3], [3, 4, 5, 6]])))
print(pretty(toRef([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]])))