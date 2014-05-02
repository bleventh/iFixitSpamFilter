from dataAcquisition import User
from dataAcquisition import Wiki

userIDs = open('UserIDs.txt', 'r')
features = open('feature.txt', 'w')



def reputationFeature(user):
   if user.reputation > 1:
      features.write('0 ')
   else:
      features.write('1 ')

def badgeCount(user):
   if user.total_badges:
      features.write('0 ')
   else:
      features.write('1 ')

for userID in userIDs:
   user = User(userID)

   #import functions for gathering here
   reputationFeature(user)
   badgeCount(user)

   features.write('\n')

features.close()
userIDs.close()
