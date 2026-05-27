class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Q1: Upper vs lower same or different?
        # Q2: Duplicates appear at least same number of times?
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            return ""
        match_req = len(set(t))

        count_s = {}
        count_t = {}
        matched = 0
        min_len = len_s + 1
        min_start = 0
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # O U Z O D Y X A Z V 
        # 0 1 2 3 4 5 6 7 8 9
        #           l     r
        # Z: 1
        # Y: 0
        # X: 1
        # matched = 2
        l, r = 0, 0
        while r < len_s:
            c_r = s[r]
            if c_r not in count_t:
                r += 1
                continue
            
            count_s[c_r] = count_s.get(c_r, 0) + 1
            print(count_s[c_r], count_t[c_r])
            if count_s[c_r] == count_t[c_r]:
                matched += 1

                print(l, r, matched, min_len, len_t)
                while l <= r and matched == match_req: # len_t:
                    c_l = s[l]
                    # just matched
                    if min_len > (r-l+1):
                        min_start = l
                        min_len = (r-l+1)
                        print(matched, min_start, min_len)

                    # start shrinking
                    if c_l in count_t:
                        if count_s[c_l] == count_t[c_l]:
                            matched -= 1
                        print(c_l, matched)
                        count_s[c_l] -= 1
                    l += 1
            print("---")
            r += 1
    
        print(min_len, len_s)
        print(s[min_start: min_len+1])
        if min_len <= len_s:
            return s[min_start: min_start+min_len]
        else:
            return "" 

# WA aa


        