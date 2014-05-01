from dataAcquisition import User
from dataAcquisition import Wiki


aUser = User(778022)

if aUser.reputation > 1:
   print "good"
else:
   print "bad"

print aUser.about_rendered

