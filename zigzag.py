
def extenderArr(s,numsRow):
    extendArr = [s[0]]
    iterator = 1
    col = True
    loop = True
    while(loop):
        if(col):
            for i in range(0,numsRow-1):
                try:
                    extendArr.append(s[iterator])
                    iterator+=1
                except:
                    break
            col = False
        else:
            for c in range(0,numsRow-1):
                for r in range(0,numsRow-2):
                    extendArr.append('')
                try:
                    extendArr.append(s[iterator])
                    iterator+=1
                except:
                    loop = False
                    break
            col=True

        if(iterator > len(s)):
            loop = False
    return extendArr
def propFormatArr(extendArr,numsRow):
    resoultArr = ''
    for i in range(0,numsRow):
        j=i
        while(True):
            try:
                if(extendArr[j] != ''):
                    resoultArr +=extendArr[j]
            except:
                break
            j+=numsRow

    return resoultArr

s = 'PAYPALISHIRING'
numsRow = 1
extendArr = extenderArr(s,numsRow)
print(propFormatArr(extendArr,numsRow))