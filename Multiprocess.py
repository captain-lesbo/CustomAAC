import multiprocessing
import pyttsx3
import keyboard

def parseShorthand(phrase, dictionary): #o(n), but this is okay as n will only be as big as number of word in sentence
    #parse phrase for any shorthands

    splitphrase = phrase.split()
    newphrase = ""
    for word in splitphrase:
        if word in dictionary: #O(1)
            newphrase = newphrase + dictionary[word]
        else:
            newphrase = newphrase + word
            newphrase = newphrase + " "
    return newphrase

def sayFunc(phrase, voice, rate, volume, dictionary): #text to speak function
    #initialise engine and load in settings
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[voice].id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    #replace shorthand words
    newphrase = parseShorthand(phrase, dictionary)

    engine.say(newphrase)
    engine.runAndWait()

def say(phrase, voice, rate, volume, dictionary): #main aac interface
    if __name__ == "__main__":
        p = multiprocessing.Process(target=sayFunc, args=(phrase, voice, rate, volume, dictionary))
        p.start()

        while p.is_alive():
            if keyboard.is_pressed('q'):
                p.terminate()
            else:
                continue
            
        p.terminate()
        
def aac():
    phrase = input(">")
    while phrase != "00":
        continue

def createShortcut():
    print("add a new shortcut to dictionary")

def loadSettings(settingsfile):
    #load in settings
    f = open(settingsfile)
    
    #read in settings line by line
    settings =  {'voice' : int(f.readline()), 'rate' : int(f.readline()), 'volume' : float(f.readline())}

    f.close()

    return settings

def loadDict(dictfile):
    #load in dictionary
    f = open(dictfile)
    
    #I don't know how to read in a dictionary like this
    #research eval() function??
    dictionary = {"buha" : "burning hands"}
    
    #close dictionary file
    f.close()

    return dictionary

def main():
    settings = loadSettings("settings.txt")

    dictionary = loadDict("dictionary.txt")

    phrase = "the quick brown fox jumped over my ass"
    
    say(phrase, settings['voice'], settings['rate'], settings['volume'], dictionary)

main()
