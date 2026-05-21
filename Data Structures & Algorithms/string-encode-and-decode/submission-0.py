class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = ''
        for s in strs:
             sizes += str(len(s)) + ','
        encoded = ''.join(strs)
        return sizes + '#' + encoded

    def decode(self, s: str) -> List[str]:
        sizes = []
        i = 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1

        i += 1
        res = []
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz

        return res


        
