class SolNR190:
    def reverseBits(self, x: int) -> int:
        x_str = str(x)
        resoultList=[]
        i=0
        for i in range(len(x_str)):
            if x_str[i]=='1':
                resoultList.append(2**i)
        for x in resoultList:
            i += x
        return i
