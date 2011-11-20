import urllib
import zipfile
import string
import random

dictionary = zipfile.ZipFile("dictionary.zip", "r").open("dictionary.txt", "r")
#   Dictionary format:
#   "English", word, type, "#", Definition

greeting = ["Hey", "Hi", "Hello", "Whats up", "Yo"]
farewell = ["Goodbye", "Bye", "See you later", "Farewell"]
thanks = ["Thanks", "Thank you", "Thanks a lot"]

topic = "Nothing"

def main():
    print "Hello"
    talk(raw_input())

def talk(a):
    a = a.capitalize()
    wordList = a.split(" ")

    if a in greeting:
        print greeting[random.randint(0,4)]
    elif a in farewell:
        endConversation()
    elif a in thanks:
        print "No problem"
    elif a == "What are you thinking about":
        print topic
    elif (wordList[0] == "What") and (wordList[1] == "are" or "is"):
        wordDefinition(wordList[-1])
    elif "weather" in wordList:
        discussWeather()
    else:
        print "yep"
        
    talk(raw_input())

def endConversation():
    print farewell[random.randint(0,3)]
    exit()

def wordDefinition(b):
    answer = "I don't know"
    for line in dictionary:
        defList = line.split()
        if (b == defList[1]) and (defList[2] == "Noun"):
            s = str(defList[4:])    #puts everything from the 4th line onward into a string
            answer = "Its " + "".join(c for c in s if c.isalnum() or c.isspace())  #Removes symbols
            topic = b
            break        
    print answer

def discussWeather():
    weatherData = urllib.urlopen("http://rss.wunderground.com/auto/rss_full/MD/Frederick.xml?units=english")
    for line in weatherData:
        if "Current Conditions" in line:
            conditions = line.split(":")
            conditions = conditions[1].split("-")
            print "Its pretty nice." + conditions[0]
        
if __name__ == '__main__':
    main()
