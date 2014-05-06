from dataAcquisition import User
from dataAcquisition import Wiki
from bs4 import BeautifulSoup as bs
import re

userIDs = open('UserIDs.txt', 'r')
features = open('feature.txt', 'w')


def noniFixitDomains(user):
   html = bs(user.about_rendered)
   urlCount = 0.0
   ifixitUrlCount = 0.0

   for a in html.find_all('a', href=True):
      if len(re.findall(r"ifixit", a['href'])):
         ifixitUrlCount = ifixitUrlCount + 1
      urlCount = urlCount + 1

   if urlCount:
      features.write('%s ' % (1.0 - (ifixitUrlCount/urlCount)))
   else:
      features.write('0 ')

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
   noniFixitDomains(user)
   reputationFeature(user)
   badgeCount(user)

   features.write('\n')

features.close()
userIDs.close()
