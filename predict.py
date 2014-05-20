from sklearn import svm

X = []
y = []
features = open('feature.txt', 'r')
labels = open('labeledUsers.txt', 'r')

for line in features:
   X.append(line.split())

for line in labels:
   y.append(line.split()[0])

clf = svm.SVC()
clf.fit(X, y)

testFeatures = open('testFeatureData.txt', 'r')
testLabels = open('labelTestData.txt', 'r')

testX = []

for line in testFeatures:
   testX.append(clf.predict(line.split())[0])

accuracyCount = 0.0
total = 0.0
for line in testLabels:
   if testX[int(total)] == '1':
      print "Guessing spam for %s" % (int(total))
   else:
      print "Guessing ham for %s" % (int(total))

   if line.split()[0] == testX[int(total)]:
      accuracyCount += 1.0
   else:
      print "Number %s is incorrect" % (int(total))
   total += 1.0

print "accuracy: %s" % (accuracyCount/total)
