import math


class SolNR6:
    def convert(self, s: str, howManyRows = 2):
        numbColumns = self.howManyColums(s, howManyRows)
        motherTab = []
        # Create motherTab
        j = 0
        for _ in range(numbColumns):
            motherTab.append([])
        for index, column in enumerate(motherTab):
            for k in range(howManyRows):
                if index % (howManyRows - 1) == 0:
                    try:
                        column.append(s[j])
                        j += 1
                    except:
                        pass
                column.append('')
                elif index + len(column[k]) == howManyRows:
                    column.append(s[j])
                    j += 1
                else:
                    column.append('')


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
