class Solution:
    def __init__(self):
        self.map = {}
        self.map['2'] = ['a', 'b', 'c']
        self.map['3'] = ['d', 'e', 'f']
        self.map['4'] = ['g', 'h', 'i']
        self.map['5'] = ['j', 'k', 'l']
        self.map['6'] = ['m', 'n', 'o']
        self.map['7'] = ['p', 'q', 'r', 's']
        self.map['8'] = ['t', 'u', 'v']
        self.map['9'] = ['w', 'x', 'y', 'z']

        self.results = []
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.results

        self.allStrings(digits, 0, "")

        return self.results
        
    def allStrings(self, digits: str, i: int, current: str) -> None:
        if i == len(digits):
            self.results.append(current)
            return

        # print(i, digits[i], self.map[int(digits[i])])
        for ch in self.map[digits[i]]:
            # print("Char", ch)
            new_str = current + ch
            self.allStrings(digits, i+1, new_str)