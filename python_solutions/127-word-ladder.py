# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordict = set(wordList)
        
        s1 = {beginWord}
        s2 = {endWord}
        n = len(beginWord)
        step = 0
        wordict.remove(endWord)
        
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i+1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return step+1
                    if w not in wordict:
                        continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
        return 0
        
"""
Runtime: 132 ms, faster than 65.80% of Python3 online submissions for Word Ladder.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Word Ladder.
"""
