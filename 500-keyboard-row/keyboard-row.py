class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [1,2,2,1,0,1,1,1,0,1,1,1,2,2,0,0,0,0,1,0,0,2,0,2,0,2]
        res = []

        for word in words:
            rowCount = defaultdict(int)
            for char in word.lower():
                rowCount[rows[ord(char) - ord('a')]] += 1
            if len(rowCount) == 1:
                res.append(word)
        return res