from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()

#1
print(emails.target_names)

#2
categories = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])

#3
print(emails.data[5])

#4
print(emails.target[5])

#5
train_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'train')

#6
test_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'test')

#7
counter = CountVectorizer()

#8
counter.fit(test_emails.data + train_emails.data)


#9

test_counts = counter.transform(test_emails.data)
#10
train_counts = counter.transform(train_emails.data)

#11
classifier = MultinomialNB()

#12
classifier.fit(train_counts,train_emails.target)

#13
print(classifier.score(test_counts,test_emails.target))#97%

#14

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = 'test')
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = 'train')

test_counts = counter.transform(test_emails.data)

train_counts = counter.transform(train_emails.data)

classifier.fit(train_counts,train_emails.target)

print(classifier.score(test_counts,test_emails.target))#output 99%
