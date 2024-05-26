import random
words = ["strawberry","melon","banana"]
word = random.choice(words)
print(word)
answer = "".join("_" for _ in word) 
continue_check = True
lives = 5


def sofar():
    print(answer)

def check(letter):
    global answer
    global lives
    checkstatus = "" 
    if letter in word:
        # Update the answer with the correct letter
        answer_list = list(answer)
        for x in range(len(word)):
            if word[x] == letter:
                answer_list[x] = letter
        answer = ''.join(answer_list)
    else:
        # Decrement lives for incorrect guess
        lives -= 1
        print(f"Incorrect guess. Lives left: {lives}")
        if lives == 0:
            checkstatus = "lose"
    return checkstatus

#continue loop
def continue_loop():
    global continue_check
    global lose
    sofar()
    letter = input("please guess a letter \n")
    lose = check(letter)
    if "_" not in answer:
        continue_check = False
        print("you win")
    if lose == "lose":
        print(f"no more lives, the word was {word}")
        continue_check = False
        
    

    
    

while continue_check == True:
    continue_loop()
