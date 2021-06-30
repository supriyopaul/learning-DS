class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        past_elements = dict()
        index = 0
        for element in nums:
            import pdb; pdb.set_trace()
            if past_elements.get(str(element)): return True
            else: past_elements[str(element)] = index
            index += 1
        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
