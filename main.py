from random_word_generator import  pick_random_word

def change_current_word_state(selected_word,input_char,current_word_state,attempts_remaining):
    modified_word_state=""
    for i in range(len(selected_word)):
        if current_word_state[i]== "_" and selected_word[i] == input_char:
            modified_word_state+=selected_word[i]
        else:
            modified_word_state+=current_word_state[i]
    return modified_word_state

       
def input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining):
    if input_char in selected_word:
        current_word_state=change_current_word_state(selected_word,input_char,current_word_state,attempts_remaining)
    else:
        attempts_remaining-=1
    return current_word_state,attempts_remaining


def print_current_state(current_word_state,attempts_remaining):
    #It will print currrent status of the game that is the alphabets selected so far and attempts left

    print("Current Word State:",end=" ")

    for i in current_word_state:
        print(i,end=" ")

    print("\t Attempts Remaining: {} ".format(attempts_remaining))


def check_game_status(selected_word,current_word_state,attempts_remaining):

    if attempts_remaining<=0:
        print ("Sorry you lost! :( Try Again!")
        print("The word was: {}".format(selected_word))
        return False
    
    if selected_word == current_word_state:
        return False
    return True


def play_game(attempts=5):
    #It will contain main logic of the game 
    
    #It will store the value of randomly picked  word
    selected_word= pick_random_word()

    #It will show present status of the word
    current_word_state = ""

    for i in selected_word:
        if i==' ' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            current_word_state+=i
        else:
            current_word_state+="_"

    attempts_remaining = attempts

    print_current_state(current_word_state,attempts)

    while True:
        input_char = input("Guess the character: ")
        print("")

        current_word_state,attempts_remaining=input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining)

        print(current_word_state,attempts_remaining)

        game_end_checker = check_game_status(selected_word,current_word_state,attempts_remaining)
        if(game_end_checker == False):
            break
        

if __name__ == "__main__":
    play_game(7)

