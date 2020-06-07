import random
from random import choice
import json

# example array of bible verses - replace with actual file/database
cache = []
TextList = ["This is one", "This is two", "Today is Saturday", "Today is Monday", "What a great day!"]
#f = open("VerseTest.txt", "r")
#ImportedText = f.read()
#f.close()
#TextList = list(ImportedText.split(", "))

# takes in import file and outputs string of bible verse
def file2string():
    size = len(TextList)
    verseNumber = random.randint(0, size - 1)
    if verseNumber in cache:
        verseNumber = choice([i for i in range(0, size -1) if i not in cache])
    verseText = TextList[verseNumber]
    cache.append(verseNumber)
    return verseText


output = json.dumps(file2string())
print(output)
