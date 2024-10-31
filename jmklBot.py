import wordManager
import WebScraper
import nltk
import time
from nltk.corpus import words



nltk.download('words')
wordList = words.words()
wordManager = wordManager.WordManager(wordList)

webScraper = WebScraper.WebScraper()

while "https://jklm.fun/" not in webScraper.getUrl():
    time.sleep(1)

    
while True:
    index = 0

    time.sleep(0.1)

    while webScraper.isMyTurn():
        wordCode = webScraper.readCode()

        if wordCode:
            time.sleep(0.1)
            try:
                word = wordManager.getWord(wordCode, index)
                print(wordCode + " : " + word)

                webScraper.inputWord(word)
                index += 1
            except:
                print("Tried  all words for the pattern")
                continue






