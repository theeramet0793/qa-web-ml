from FetchData import fetch_data_from_facebook_db
from WordTokenize import wordTokenize
from Save2DB import saveKeyword2db
from CountKeyword import countKeyword

# Start 
fetch_data = fetch_data_from_facebook_db()
#print(fetch_data)
id = fetch_data[0][0]
tmdbId = fetch_data[0][1]
detail = fetch_data[0][2]

keywordList = wordTokenize(detail)
print(keywordList)

tableName1 = 'moviefromfbg'
tableName2 = 'moviefromimdb'
tableName3 = 'moviefromyt'
saveKeyword2db(tableName1,id,keywordList,tmdbId)
countKeyword(keywordList)