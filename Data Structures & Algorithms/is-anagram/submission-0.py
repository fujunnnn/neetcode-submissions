class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}

        if len(s) != len(t):
            return False

        for char in s:
            map_s[char] = map_s.get(char, 0) + 1


        for char in t:
            count = map_s.get(char, 0)

            if count == 0 or char not in map_s:
                return False
            map_s[char] = map_s.get(char, 0) - 1
        return True