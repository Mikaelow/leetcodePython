class Solution:
    def check_strings(self,resoult : str, string : str):
        if resoult == string:
            return True
        else:
            return False
        
    def base_divided_str(self, base: str, string: str):
        resoult = ''
        i = 0
        j = 0
        while i<len(base):
            while j<len(string):
                if string[j] == base[i]:
                    resoult = resoult + string[j]
                    j = 0
                    break
                else:
                    j = j + 1
            i = i + 1
        
        return self.check_strings(resoult,base)
     
    def string_smaller_part(self, string : str):
        return string
        

    def gcdOfStrings(self, str1: str, str2: str):
        is_base_divided = self.base_divided_str(str1,str2)
        if is_base_divided:
            return self.string_smaller_part(str2)
        else:
            return ''



if __name__ == '__main__':
    str1 = "ABCAABCAABCAABCA"
    str2 = "ABCAABCA"
    print(Solution().gcdOfStrings(str1,str2)) 