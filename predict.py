from dataAcquisition import User
from dataAcquisition import Wiki

userIDs = open('UserIDs.txt', 'r')
features = open('feature.txt', 'w')

def reputationFeature(user):
   if user.reputation > 1:
      features.write('0 ')
   else:
      features.write('1 ')


for userID in userIDs:
   user = User(userID)
   reputationFeature(user)
   #import functions for gathering here

   features.write('\n')
