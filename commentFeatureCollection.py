from dataAcquisition import Comment
import Utils
import time
import sys

if len(sys.argv) != 3:
	sys.exit('2 arguments required: {commentIDListFile} {outputFile}')

commentIDs = open(sys.argv[1], 'r')
features = open(sys.argv[2], 'w')

def rating(comment):
	rating = comment.rating

	if rating >= 0:
		features.write('0 ')
	else:
		features.write('1 ')

"""def numReplies(comment):
	replies = comment.replies

	if replies:
		features.write('0 ')
	else:
		features.write('1 ')

def author(comment):
	#check if author is a spam user"""

for commentID in commentIDs:
	comment = Comment(commentID)

	#add this for api rate-limiting purposes
	time.sleep(0.1)

	#run feature collection
	if comment.text_rendered:
		Utils.noniFixitDomains(user.text_rendered)
	else:
		features.writes('1 ')

	rating(comment)
	#numReplies(comment)
	#author(comment)