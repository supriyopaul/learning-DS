class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer == len(s): return True
            t_pointer += 1
        return False

if __name__ == "__main__":
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))
    print(Solution().isSubsequence(s="bb", t="ahbgdc"))