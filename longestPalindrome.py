class SolNR5:
    def longestPalindrome2(self, s: str):
        resoult = []
        for i in range(len(s)):
            resoultFirst = []
            resoultSecond = []
            j = i
            k = i
            while j > -1 and k < len(s):
                if s[j] == s[k]:
                    resoultFirst = s[j:k + 1]
                    j -= 1
                    k += 1
                else:
                    break
            k = i+1
            j = i
            while j > -1 and k < len(s):
                if s[j] == s[k]:
                    resoultSecond = s[j:k+1]
                    j -= 1
                    k += 1
                else:
                    break
            if len(resoultFirst) > len(resoultSecond):
                resoult = max([resoult, resoultFirst], key=len)
            else:
                resoult = max([resoult, resoultSecond], key=len)
        return resoult
