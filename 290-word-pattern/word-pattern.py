class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDict = {}
        wordDict = {}
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in patternDict:
                if words[i] != patternDict[pattern[i]]:
                    return False
            elif words[i] in wordDict:
                if pattern[i] != wordDict[words[i]]:
                    return False
            else:
                patternDict[pattern[i]] = words[i]
                wordDict[words[i]] = pattern[i]
            
        return True