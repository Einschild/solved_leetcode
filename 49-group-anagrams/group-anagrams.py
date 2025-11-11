class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for anagram in strs:
            freq = [0] * 26

            for char in anagram:
                freq[ord(char) - ord('a')] += 1
            
            res[tuple(freq)].append(anagram)
        
        return list(res.values())