class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}

        for letter in s:
                map1[letter] = 1 + map1.get(letter, 0)

        for letter in t:
                map2[letter] = 1 + map2.get(letter, 0)

        return map1==map2