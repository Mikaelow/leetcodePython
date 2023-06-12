from typing import List


class SolNR744:
    def solution(self, letters: List[str], target: str) -> str:
        fullAlphabet = 'abcdefghijklmnopqrstuvwxyz'
        startOfAlphabeth = fullAlphabet.find(target)
        alphabet = fullAlphabet[startOfAlphabeth+1:]
        positions ={}
        for letter in letters:
            if letter == target:
                pass
            else:
                position = alphabet.find(letter)
                difference = abs(alphabet.find(target)-position)
                positions[difference] = letter
        for i in range(32):
            if positions.get(i) != None:
                return positions.get(i)
            else:
                pass