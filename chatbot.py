import urllib
import zipfile
import string

dictionary = zipfile.ZipFile("dictionary.zip", "r").open("dictionary.txt", "r")
#   Dictionary format:
#   "English", word, type, "#", Definition

def main():
    print "Hello"
    talk(raw_input())

def talk(a):
    a = a.capitalize()
    wordList = a.split(" ")
    if (wordList[0] == "What") and (wordList[1] == "are" or "is"):
        wordDefinition(wordList[-1])
    if a == "goodbye":
        endConversation()
    talk(raw_input())

def endConversation():
    print "Bye"
    exit()

def wordDefinition(b):
    for line in dictionary:
        defList = line.split()
        if b in defList[1] and defList[2] == "Noun":
            s = str(defList[4:])
            print "Its " + "".join(c for c in s if c.isalnum() or c.isspace())
            break

if __name__ == '__main__':
    main()
