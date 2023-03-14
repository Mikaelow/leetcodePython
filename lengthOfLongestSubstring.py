class SolNR3:
    def returnFucn(self, s:str):
        counterList = []
        counter = 0
        curentStr = []
        for i in s:
            if i in curentStr:
                counterList.append(counter)
                counter = 1
            else:
                counter = counter + 1
            curentStr.append(i)
        counterList.append(counter)
        return max(counterList)
    def lengthOfLongestSubstring(self, s):
        normal = self.returnFucn(s)
        backward = self.returnFucn(s[::-1])
        return max(normal, backward)