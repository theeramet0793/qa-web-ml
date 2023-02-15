from pythainlp.tokenize import word_tokenize
from pythainlp.spell import NorvigSpellChecker


def wordTokenize(text):
  l1 = word_tokenize(text, engine="newmm")
  l2 = list(set(l1))
  keywordList = removeEmptyStringAndCheck(l2)
  return keywordList

def removeEmptyStringAndCheck(stringList):
  index = 0
  checker = NorvigSpellChecker()
  for item in stringList:
    if(item == ' '):
      stringList.pop(index)
    elif(checker.prob(item)==0):
      stringList.pop(index)
    index+=1
  
  return stringList