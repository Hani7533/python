import random
import hungman_structure

word_list = ["education" , "university" , "programming" , "computer" , "harita" , "python" , "engineering" , "apple" , "clg"]
attemt = 6

guess = random.choice(word_list)
print(guess)


display = []

for i in range(len(guess)):
    display += "_"
print(display) 

game_over = False
while not game_over:
    
    guessed_letter = input("guess a word: ").lower()
    
    for position in range(len(guess)):
        letter = guess[position]
        
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
            
    if guessed_letter not in guess:
        attemt -=1
        
        if attemt == 0:
            game_over = True
            print("you lose !!!!!!")
    
    if "_" not in display:
        game_over = True
        print("you win !!!!")
    
    print(hungman_structure.Stages[attemt])