import math


class SolNR6:
    def convert(self, s: str, howManyRows = 2):
        table=self.fillTable(s,howManyRows)

        return self.returningStrint(table)
    def fillTable(self,s,howManyRows):
        numbColumns = self.howManyColums(s, howManyRows)
        motherTab = []
        j = 0
        nextPosition = howManyRows - 1
        for _ in range(numbColumns):
            motherTab.append([])
        for index, column in enumerate(motherTab):
            for i in range(howManyRows):
                if nextPosition == howManyRows - 1 or nextPosition == 0:
                    try:
                        column.append(s[j])
                        j += 1
                    except:
                        pass
                elif i == nextPosition:
                    column.append(s[j])
                    j += 1
                else:
                    column.append('')
            if nextPosition == 1 or nextPosition == 0:
                nextPosition = howManyRows - 1
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
    def returningStrint(self,table: list):
        string=''
        j=0
        for i in range(len(table[j])):
            for j in range(len(table)):
                try:
                    string +=table[j][i] + ''
                except:
                    pass

        return string


