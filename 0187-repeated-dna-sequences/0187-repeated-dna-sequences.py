class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or s < 10:
            return []

        seen = {}
        result = set()

        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                result.add(sub)
            else:
                seen[sub] = 1

        return list(result)

