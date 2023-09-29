class Solution:
    def __init__(self) -> None:
        pass
    def divisor(string : str) -> str:
        memory = ''
        for s in string:
            if s in memory:
                break
            else:
                memory = memory + s
        return memory
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        resoult = ''
        shorter_string = min(str1,str2)
        longer_string = max(str1,str2)
        for char_low_str in shorter_string:
            if char_low_str in longer_string:
                resoult = resoult + char_low_str
            else:
                break
        return Solution.divisor(resoult)



if __name__ == '__main__':
    str1 = "ABCDEF"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1,str2)) 