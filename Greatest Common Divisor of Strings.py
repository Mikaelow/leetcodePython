class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        resoult = ''
        shorter_string = min(str1,str2)
        longer_string = max(str1,str2)
        for char_low_str in shorter_string:
            if char_low_str in longer_string:
                resoult = resoult + char_low_str
            else:
                break
        return resoult
 

if __name__ == '__main__':
    str1 = "ABABABAB"
    str2 = "ABAB"
    print(Solution().gcdOfStrings(str1,str2)) 