class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_size = len(s)
        for i in range(ints_size/2):
            s[i], s[s_size-1] = s[s_size-1], s[i]

print(Solution().reverseString(["h","e","l","l","o"]))
