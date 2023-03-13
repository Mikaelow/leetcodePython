import string
class SolNR:
    def lengthOfLongestString(self, s: str):
        try:
            alphabet = string.ascii_lowercase
            i = 1
            counter = 1
            listOfK=[]
            position = alphabet.find(s[0])
            while i < len(s):
                if position < alphabet.find(s[i]):
                    counter = counter + 1
                else:
                    listOfK.append(counter)
                    counter = 1
                position = alphabet.find(s[i])
                i = i + 1


            listOfK.append(counter)
            position = alphabet.find(s[0])
            counter = 1
            i = 1
            while i < len(s):
                if position > alphabet.find(s[i]):
                    counter = counter + 1
                else:
                    listOfK.append(counter)
                    counter = 1
                position = alphabet.find(s[i])
                i = i + 1
            listOfK.append(counter)
            return max(listOfK)
        except:
            return 0