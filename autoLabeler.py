from appscript import *
import sys

if len(sys.argv) != 3:
   sys.exit("Takes two arguments {userID file} {outputFile}")

safari = app("Safari")

userIDs = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

print "Press q to quit\n"

for line in userIDs:
   safari.make(new=k.document, with_properties={k.URL:
      'http://www.ifixit.com/user/%s' % (line)})

   answer = raw_input("Is this spam? (y/n): ")
   if answer == 'y':
      output.write('1\n')
   elif answer == 'q':
      safari.windows.first.current_tab.close()
      break
   else:
      output.write('0\n')
   safari.windows.first.current_tab.close()

print "Thank you for your input"
