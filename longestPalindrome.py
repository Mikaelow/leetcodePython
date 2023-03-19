class SolNR5:
    def longestPalindrome(self, s:str):
        nChars = 1
        resoults = []
        #loop for i size of curentString
        while nChars < len(s):
            for startOfRange in range(len(s)-nChars):
                curentString = []
                reverseString = []
                for i in range(startOfRange, startOfRange+nChars+1):
                    curentString.append(s[i])
                    reverseString.append(s[i])
                reverseString.reverse()
                if curentString == reverseString:
                    resoults.append(''.join(curentString))
                else:
                    pass

            nChars = nChars+1
        try:
            return max(resoults, key=len)
        except:
            return '' if len(s) == 0 else ''.join(s[0])

