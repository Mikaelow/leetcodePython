class SolNR3:
    def returnFucn(self, s:str):
        counterList = []
        counter = 0
        curentStr = []
        for i in s:
            if i in curentStr:
                counter = len(curentStr)
                counterList.append(counter)
                positionOfNextSameChar = curentStr.index(i)+1
                for j in range(positionOfNextSameChar):
                    curentStr.pop(0)
            curentStr.append(i)
        counter = len(curentStr)
        counterList.append(counter)
        return max(counterList)
    def lengthOfLongestSubstring(self, s):
        normal = self.returnFucn(s)
        backward = self.returnFucn(s[::-1])
        return max(normal, backward)