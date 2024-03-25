
import random

fruits = ["abacate","abacaxi", "acrola", "amora",
          "banana",
          "caju","caqui","carambola","cereja","coco",
          "damasco",
          "figo","framboesa",
          "goiaba","graviola",
          "jabuticaba","jaca","jenipapo",
          "kiwi",
          "laranja","lima","limao",
          "mamao", "manga","melancia","melao","morango", 
          "pequi","pera", "pessego", "pitanga", "pitaya", 
          "roma",
          "tamarindo","tangerina","tomate", 
          "umbu",  "uva" ]
mistakes = 0

#choice fruit 
def randomWord(fruits):
    position = random.randint(0, len(fruits) - 1)
    return fruits[position]
    

#start game
def start(word): 
    for i in range(len(word)):
        print("__", end="  ") 
    print("\n")

choiceFruit = randomWord(fruits)
word = ["__"]*len(choiceFruit)
start(word)

while(mistakes < 6):
    letter = input(("Letra: ").lower())
    found = False
    for i in range(len(choiceFruit)):
        if(choiceFruit[i] == letter):
            word[i] = letter
            found = True
    if not found:
        mistakes += 1
    for letter in word:
        if (letter != "__"): print(letter, end="  ")
        else: print("__", end="  ")
    print("\n")
    if "__" not in word:
        print("Você ganhou!")
        break
    print(str(mistakes) + " de 6 tentivas")
    if(mistakes == 6):
        print("Você perdeu! A palavra era " + choiceFruit )
        break


