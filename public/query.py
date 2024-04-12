import re
import sys
import json
import pickle

# Argumen check
if len(sys.argv) != 4 :
	print ("\n\nPenggunaan\n\tquery.py [index] [n] [query]..\n")
	sys.exit(1)

query = sys.argv[3].split(" ")
n = int(sys.argv[2])

with open(sys.argv[1], 'rb') as indexdb:
	indexFile = pickle.load(indexdb)

# Query
list_doc = {}
for q in query:
	try :
		for doc in indexFile[q]:
			if doc['Place_Id'] in list_doc :
				list_doc[doc['Place_Id']]['Score'] += doc['Score']
			else :
				list_doc[doc['Place_Id']] = doc
	except :
		continue

# Convert to list
list_data=[]
for data in list_doc :
	list_data.append(list_doc[data])

# Sorting list descending
count=1;
for data in sorted(list_data, key=lambda k: k['Score'], reverse=True):
	y = json.dumps(data)
	print(y)
	if (count == n) :
		break
	count+=1