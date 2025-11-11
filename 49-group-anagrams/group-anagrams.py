class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for anagram in strs:
            freq = [0 for _ in range(26)]

            for char in anagram:
                freq[ord(char) - 97] += 1
            
            res.setdefault(tuple(freq), []).append(anagram)
        
        return list(res.values())