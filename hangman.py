import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 7
word_list = ["aardvark", "baboon", "camel", "mouse", "elephant", "keyboard", "softuni", "laptop", "phone", "intel", "core", "case", "lion", "rat", "book", "mousepad", "fridge"]
chosen_word = random.choice(word_list)
display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives -= 1
        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        elif lives == 0:
            print(stages[0])
            print("You lose")
            quit()

    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You win")