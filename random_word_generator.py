from random import randint
def pick_random_word():
    word_list=["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone","computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]
    selected_index=randint(0,len(word_list)-1)
    return word_list[selected_index]

print(pick_random_word()) 