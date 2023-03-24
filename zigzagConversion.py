import math
class SolNR6:
    def convert(self, s:str, numRows=2):
        numColums=self.howManyColums(s, numRows)
        motherTab=[]
        #Create motherTab
        j=0
        for _ in range(numColums):
            motherTab.append([])
        for i in motherTab:
            try:
                for k in range(numRows):
                    i.append(s[k+j])
            except:
                pass
            j += numRows


        return motherTab


    def howManyColums(self, s:str, numRows):
        return math.ceil(len(s)/numRows)