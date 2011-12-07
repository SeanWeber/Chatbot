#    Python Chatbot
#    Copyright (C) 2011  Sean Weber, Wesley Wiser
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import zipfile
import string
import random
import aiml

dictionary = zipfile.ZipFile("dictionary.zip", "r").open("dictionary.txt", "r")
#   Dictionary format:
#   "English", word, type, "#", Definition

greeting = ["Hey", "Hi", "Hello", "Whats up", "Yo"]
farewell = ["Goodbye", "Bye", "See you later", "Farewell"]
thanks = ["Thanks", "Thank you", "Thanks a lot"]
questions = ["What do you think about {0}?", "I don't really like {0}. Do you?", "I like {0}, don't you?", "Why do you say {0}?"]

topic = "Nothing"

k = aiml.Kernel()
k.learn("aiml2.xml")

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
        
    elif (wordList[0] == "What") and (wordList[1] == "are" or "is") and (wordList[2] != "your"):
        wordDefinition(wordList[-1])
        
    elif "weather" in wordList:
        discussWeather()
        
    elif "i think" in a.lower():
        print "Why do you think that?"
        
    #elif a.lower().split(" ")[0] == "yes":
    #    print "That's good"
        
    #elif a.lower().split(" ")[0] == "no":
    #    print "Really?"
        
    #elif isStatement(a):
    #    print questions[random.randint(0, 3)].format(getNoun(a))
        
    elif a.endswith("?"):
        if a.lower().startswith("why"):
            print "I don't know, how{0}".format(getWhyQuestionChunk(a.lower()))
        elif "are you a" in a.lower():
            print ["yes", "no"][random.randint(0, 1)]
        else:
            print "I don't know, {0}".format(a.lower())
            
    else:
        b = a.upper()
        k.respond(b)
        print k.respond(a)

            
        #print ["yep", "really?"][random.randint(0, 1)]
        
    talk(raw_input())
    
def getWhyQuestionChunk(s):
    chunk = s.lower()
		
    if chunk.startswith("why"):
        chunk = chunk.replace("why", "", 1)
			
    if chunk.startswith("do"):
        chunk = chunk.replace("do", "", 1)
			
    if chunk.startswith("are"):
        chunk = chunk.replace("are", "", 1)
        print "hit"
    return chunk
    
def isStatement(s):
    first = s.split(" ")[0].lower()
		
    a = first != "what" and first != "how" and first != "why" and first != "who" and first != "where" and not s.endswith("?")
    #print a 
    return a
		
def getNoun(s):
    words = s.split(" ")
		
    #get the first noun in the sentence
    for word in words:
        lower = word.lower()
        if lower != "a" and lower != "an" and lower != "the" and lower != "i" and lower != "he" and lower != "you" and lower != "she" and lower != "we":
            for line in dictionary:
                defList = line.split()
                if(lower == defList[1].lower() and (defList[2] == "Noun" or defList[2] == "Proper")): return word #"Proper Noun"s are also nouns
    return "that"

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
            print "Its pretty nice. Its " + conditions[0]
        
if __name__ == '__main__':
    main()
