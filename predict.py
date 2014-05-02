from dataAcquisition import User
from dataAcquisition import Wiki

users = open('UserIDs.txt', 'r')

for line in users:
   user = User(line)
   print user.about_rendered

   #import functions for gathering here
