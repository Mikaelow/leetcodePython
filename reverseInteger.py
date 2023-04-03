class SolNR7:
    def reverse(self, x: int) -> int:
        xStringList = self.splitString(x)
        reversedList = []
        if xStringList[0] == '-':
            reversedList.append('-')
            xStringList.pop(0)
        xStringList.reverse()
        for i in xStringList:
            if i == '0':
                pass
            else:
                reversedList.append(i)
        try:
            return int(''.join(reversedList))
        except:
            return x

    def splitString(self, x: int) -> list:
        string = str(x)
        return [i for i in string]
