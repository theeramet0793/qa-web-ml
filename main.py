from ClassFetchData import fetch_data_from_facebook_db, fetch_data_from_imdb_db, fetch_data_from_yt_db
from FuncWordTokenize import wordTokenize
from FuncSave2DB import saveKeyword2db
from FuncCountKeyword import countKeyword

# Start 
#fetch_data = fetch_data_from_facebook_db()
fetch_data = fetch_data_from_imdb_db()
#fetch_data = fetch_data_from_yt_db()

#print(fetch_data)
id = fetch_data[0][0]
tmdbId = fetch_data[0][1]
detail = fetch_data[0][2]

keywordList = wordTokenize(detail)
print(keywordList)

tableName1 = 'moviefromfbg'
tableName2 = 'moviefromimdb'
tableName3 = 'moviefromyt'
saveKeyword2db(tableName2,id,keywordList,tmdbId)
countKeyword(keywordList)