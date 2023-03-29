import math


class SolNR6:
    def convert(self, s: str, howManyRows = 2):
        numbColumns = self.howManyColums(s, howManyRows)
        motherTab = []
        j = 0
        nextPosition=howManyRows-1
        for _ in range(numbColumns):
            motherTab.append([])
        for index,column in enumerate(motherTab):
            for i in range(howManyRows):
                if nextPosition == howManyRows-1 or nextPosition==0:
                    try:
                        column.append(s[j])
                        j += 1
                    except:
                        pass
                elif i == nextPosition:
                    column.append(s[j])
                    j+=1
                else:
                    column.append('')
            if nextPosition == 1 or nextPosition == 0:
                nextPosition=howManyRows-1
            else:
                nextPosition -= 1
        return motherTab

    def howManyColums(self, s: str, numRows):
        counter = 0
        i = 0
        while i < len(s):
            if counter % numRows == 0:
                i += numRows
            else:
                i += 1
            counter += 1
        return counter - 1
