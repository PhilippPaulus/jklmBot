from typing import Optional, List


class WordManager:
    def __init__(self, wordList: List = []) -> None:
        self.hashmap = {}

        for word in wordList:
            self.addWord(word)    

    def addWord(self, word: str):
        word = word.lower()

        for i in range(len(word) - 2):
            key = word[i:i+3]
            if not self.hashmap.get(key, None):
                self.hashmap[key] = set()
            self.hashmap[key].add(word)
        
        for i in range(len(word) - 1):
            key = word[i:i+2]
            if not self.hashmap.get(key, None):
                self.hashmap[key] = set()
            self.hashmap[key].add(word)

    def removeWord(self, word: str):
        for i in range(len(word) - 2):
            key = word[i:i+3]

            if not self.hashmap[key]:
                continue            
            if not word in self.hashmap[key]:
                continue

            self.hashmap[key].remove(word)

    def getWord(self, pattern: str, index: int) -> Optional[str]:  
        wordList = list(self.hashmap.get(pattern.lower(), set()))

        if not wordList:
            return None

        return wordList[index]
    
    def __str__(self) -> str:
        return str(self.hashmap)
