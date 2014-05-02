from sklearn import svm

X = []
y = [0, 1, 1, 1]
features = open('feature.txt', 'r')

for line in features:
   X.append(line.split())

clf = svm.SVC()
clf.fit(X, y)

