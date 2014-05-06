from dataAcquisition import User
from dataAcquisition import Wiki

ABOUT_MIN_WORD_COUNT = 20
ABOUT_MAX_WORD_COUNT = 500
SUMMARY_MIN_WORD_COUNT = 10
SUMMARY_MAX_WORD_COUNT = 200

userIDs = open('UserIDs.txt', 'r')
features = open('feature.txt', 'w')

# repuation = 0
# total_badges = 0
# about_word_count = 0
# summary_word_count = 0
# summary = ""
# teams = 0


def reputationFeature(user):
   reputation = user.reputation
   if reputation > 1:
      features.write('0 ')
   else:
      features.write('1 ')

def badgeCount(user):
   total_badges = user.total_badges
   if total_badges:
      features.write('0 ')
   else:
      features.write('1 ')

def wordCount(text):
   if text:
      return len(text.split())
   else: 
      return 0 

def aboutWordCount(user):
   about_word_count = wordCount(user.about_raw)

   if about_word_count > ABOUT_MIN_WORD_COUNT and about_word_count < ABOUT_MAX_WORD_COUNT:
      features.write('0 ')
   else:
      features.write('1 ')

   print( "about: %s" % (about_word_count))

def summaryWordCount(user):
   summary = user.summary
   summary_word_count = wordCount(user.summary)

   if summary_word_count > SUMMARY_MIN_WORD_COUNT and summary_word_count < SUMMARY_MAX_WORD_COUNT:
      features.write('0 ')
   else:
      features.write('1 ')

   print( "summary: %s" % (summary_word_count))

def numTeams (user):
   teams = user.teams
   if teams:
      features.write('0 ')
   else:
      features.write('1 ')

for userID in userIDs:
   user = User(userID)

   #import functions for gathering here
   reputationFeature(user)
   badgeCount(user)
   aboutWordCount(user)
   summaryWordCount(user)
   numTeams(user)

   features.write('\n')

features.close()
userIDs.close()
