from dataAcquisition import Comment
import Utils
import time
import sys

if len(sys.argv) != 3:
	sys.exit('2 arguments required: {wikiIDListFile} {outputFile}')

wikiIDs = open(sys.argv[1], 'r')
features = open(sys.argv[2], 'w')

for wikiID in wikiIDs:
	wiki = Wiki(wikiID)

	#add this for api rate-limiting purposes
	time.sleep(0.1)

	#run feature collection
	