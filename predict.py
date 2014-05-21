from sklearn import svm
from termcolor import colored
import sys

if len(sys.argv) != 5:
   sys.exit('4 arguments required: {trainingData} {trainingLabelData}' \
             '{testData} {labeledTestData}')

X = []
y = []
features = open(sys.argv[1], 'r')
labels = open(sys.argv[2], 'r')

for line in features:
   X.append(line.split())

for line in labels:
   y.append(line.split()[0])

clf = svm.SVC()
clf.fit(X, y)

testFeatures = open(sys.argv[3], 'r')
testLabels = open(sys.argv[4], 'r')

testX = []

for line in testFeatures:
   testX.append(clf.predict(line.split())[0])

accuracyCount = 0.0
total = 0.0
for line in testLabels:
   if testX[int(total)] == '1':
      print(colored("Guessing spam for %s" % (int(total)), 'red'))
   else:
      print(colored("Guessing ham for %s" % (int(total)), 'green'))

   if line.split()[0] == testX[int(total)]:
      accuracyCount += 1.0
   else:
      print "Number %s is incorrect" % (int(total))
   total += 1.0

print "accuracy: %s" % (accuracyCount/total)
