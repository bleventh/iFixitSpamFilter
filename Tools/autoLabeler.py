from appscript import *
import sys
import os

if len(sys.argv) != 3:
   sys.exit("Takes two arguments {userID file} {outputFile}")

safari = app("Safari")

userIDs = open(sys.argv[1], 'r')

# if output file exist append to features and skip users already labeled
# else write to new blank file
linesToSkip = 0
if os.path.isfile(sys.argv[2]):
   output = open(sys.argv[2], 'r')
   for line in output:
      linesToSkip += 1
   output.close
   output = open(sys.argv[2], 'a')
else:
   output = open(sys.argv[2], 'w')

print "Press q to quit\n"

safari.make(new=k.document, with_properties={k.URL:
      'http://www.ifixit.com/'})

for line in userIDs:

# if appending to file skip the userids already labeled
   if linesToSkip > 0:
      linesToSkip -= 1
      continue

   safari.windows.first.current_tab.URL.set('http://www.ifixit.com/user/%s'
                                             % (line))

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
