from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {k:0 for k in need}
        
        result = ""
        result_window = ()

        window_start, window_end = 0, 0
        min_window_size = 0

        while window_start < len(s):
            import pdb; pdb.set_trace()
            
            if s[window_end] in need:
                have[s[window_end]] += 1
                if need == have:
                    current_min_window_size = min_window_size
                    min_window_size = min(min_window_size, window_end-window_start+1)
                    if min_window_size != current_min_window_size:
                        result_window = (window_start, window_end)
                        print(result_window)
                    while s[window_start] not in need:
                        window_start += 1
                    window_start += 1
                else:
                    window_end += 1
                print(have)

        return result_window


    
if __name__ == '__main__':
    sol = Solution()
    
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t)) # BANC

    s = "a"
    t = "a"
    print(sol.minWindow(s, t)) # a

    s = "a"
    t = "aa"
    print(sol.minWindow(s, t)) # ""