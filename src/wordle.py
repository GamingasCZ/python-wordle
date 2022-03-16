allWords = []
def generateWord():
    global allWords
    with open("words.txt", "r") as f:
        allWords = list(map(lambda x: x.strip(), f.readlines()))
        return random.choice(allWords)

def getInput():
    word = input("Word: ")
    if len(word) == 5 and word in allWords:
        return word
        
def checkInput(attempt, word):
    good = [0, 0, 0, 0, 0]
    
    for letterA, letterW, ind in zip(attempt, word, range(5)):
        if letterA == letterW:
            good[ind] = 2
        elif letterA in word:
            good[ind] = 1
            
    return good
    
def colorizeLetter(letter, color):
    if color == None: return letter
    
    labels = ("green", "gold")
    colors = ("\033[0;32m", "\033[1;33m")
    return colors[labels.index(color)] + letter + "\033[0m"
    
def clear():
    os.system("clear")

def main(args):
    word = generateWord()
    tries = []
    GAME = True
    lettersUsed = set()
    contains = set()
    confirmed = ["?","?","?","?","?"]
    
    while GAME:
        clear()
        print(f" - Used letters: {', '.join(lettersUsed)}\n - Attempts left: {6-len(tries)}\n - Contains: {', '.join(contains)}\n - Confirmed: {' '.join(confirmed)}\n")
        for i in tries:
            print("".join(i))
        
        attempt = getInput()
        if attempt == None:
            continue
        if 5-len(tries) == 0:
            GAME = False
        
        letterArray = [i for i in attempt]
        for valid, ind in zip(checkInput(attempt, word), range(5)):
            lettersUsed.add(letterArray[ind])
            if valid != 0:
                colorPick = (None, "green", "gold")[valid]
                letterArray[ind] = colorizeLetter(letterArray[ind], colorPick)
                
                if valid == 1: contains.add(letterArray[ind])
                elif valid == 2: 
                    confirmed[ind] = letterArray[ind]
                    if letterArray[ind] in contains:
                        contains.remove(letterArray[ind])
            
        tries.append(letterArray)
    
    print("\n - You failed! The word was: " + word)
    return 0

if __name__ == '__main__':
    import sys, os, random
    sys.exit(main(sys.argv))
