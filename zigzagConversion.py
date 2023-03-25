import math


class SolNR6:
    def convert(self, s: str, numRows=2):
        numColums = self.howManyColums(s, numRows)
        motherTab = []
        # Create motherTab
        j = 0
        for _ in range(numColums):
            motherTab.append([])
        for index, column in enumerate(motherTab):
            if index % (numRows - 1) == 0:
                try:
                    for k in range(numRows):
                        column.append(s[k + j])
                    j += numRows
                except:
                    pass
        return numColums

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
