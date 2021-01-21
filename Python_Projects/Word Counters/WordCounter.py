import operator
import sys

#read the file
file = open(sys.argv[1],"r")
text = file.read()
file.close()

#print(text)
#print(sys.argv)

#count the words
words = {}
for word in text.split():
    #print(word)
    if word.lower() in words:
        words[word.lower()] +=1
    else:
        words[word.lower()] = 1

sortedWords = sorted(words.items(), key = operator.itemgetter(1), reverse=True)
#print(sortedWords)

# write a counted words into the new file
file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:],"w")
file.write("Total Words - {}\nUnique Words - {}\n\n".format(len(text.split()),len(sortedWords)))

for wordInfo in sortedWords:
    file.write("{} - {}\n".format(wordInfo[0],wordInfo[1]))



file.close()
