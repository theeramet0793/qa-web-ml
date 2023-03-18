from pythainlp.tokenize import word_tokenize
from pythainlp.spell import NorvigSpellChecker
from pythainlp.spell import spell
import collections

def wordTokenize(text):
  l1 = word_tokenize(text, engine="newmm")
  #l2 = list(set(l1))
  keywordList = removeIfNotThaiWord(l1)
  return keywordList

def removeIfNotThaiWord(stringList):
  new_list = [item for item in stringList if (item != '\n' and item != '' and item != ' ' and item != '   ' )]
  return new_list

def countDuplicate(wordList):
  distinct_word_list = list(set(wordList))
  object_list = []
  
  for word in distinct_word_list:
    d = collections.OrderedDict()
    d['word'] = word
    d['freq'] = wordList.count(word)
    object_list.append(d)
  return object_list