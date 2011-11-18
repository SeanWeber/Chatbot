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
    elif a == "goodbye":
        endConversation()
    else:
        print "yep"
    talk(raw_input())

def endConversation():
    print "Bye"
    exit()

def wordDefinition(b):
    answer = "I don't know"
    for line in dictionary:
        defList = line.split()
        if (b == defList[1]) and (defList[2] == "Noun"):
            s = str(defList[4:])    #puts everything from the 4th line onward into a string
            answer = "Its " + "".join(c for c in s if c.isalnum() or c.isspace())  #Removes symbols
            break        
    print answer

if __name__ == '__main__':
    main()
