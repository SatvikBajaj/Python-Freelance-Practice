#This program simply excuctes a word scramble game

print ("Hello welcome to word scramber ...")
print ("This game simply takes an input word and scrambles it for you !")
print ("***************************************************************")
print ("***************************************************************")

#Global Variables 
play = True 
lstword = []
newword = []

#Main Code
while play: 
    word = input(str("Enter any word you want: "))
    try:
        #Variable Reset
        lstword = []
        newword = []
        lstword = list(word)
        for i in range(len(word)):
            newword.append(lstword[-i])
            newwordstr = ''.join(newword)
        print ("Your word scrambled is ",newwordstr,"!")
    except:
        print ("You broke the game oopsie!!!")