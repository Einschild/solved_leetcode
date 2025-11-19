class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        matched = {}

        for char, word in zip(pattern, words):
            patternKey = ('pattern', char)
            wordKey = ('word', word)

            if patternKey in matched and matched[patternKey] != word:
                return False
            elif wordKey in matched and matched[wordKey] != char:
                return False

            matched[patternKey] = word
            matched[wordKey] = char
            
        return True