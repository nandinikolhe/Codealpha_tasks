import random  # Importing the random module to randomly select a word

# Define a list of possible words for the game
word_list = ["Computer", "Science", "Engineering"]

lives = 5  # Initialize the number of lives to 5 (player can make 5 incorrect guesses)
chosen_word = random.choice(word_list)  # Randomly select a word from the list
print(chosen_word)  # Print the chosen word (for debugging purposes, remove this in the final game)

display = []  # Initialize an empty list to store the display of the word (with blanks for unguessed letters)

# Create the initial display list, with underscores representing unguessed letters
for i in range(len(chosen_word)):  # Loop through each letter in the chosen word
    display += '_'  # Add an underscore for each letter in the word to represent an unguessed letter

print(display)  # Print the initial display (e.g., ['_', '_', '_', '_', '_'])

game_over = False  # Initialize the game status as not over

# Start the game loop, which continues until the game is over
while not game_over:
    guessed_letter = input("Guess a letter: ")  # Prompt the player to guess a letter (input is a string)

    # Check each position in the chosen word
    for position in range(len(chosen_word)):  # Loop through each index of the word
        letter = chosen_word[position]  # Get the letter at the current position in the word
        if letter == guessed_letter:  # If the guessed letter matches the letter at the current position
            display[position] = guessed_letter  # Replace the underscore with the guessed letter at the correct position
    
    print(display)  # Print the current state of the display (e.g., ['p', '_', '_', 'l', '_'])

    # If the guessed letter is not in the word, subtract 1 from the number of lives
    if guessed_letter not in chosen_word:
        lives -= 1  # Decrease lives by 1 if the guessed letter is incorrect
        if lives == 0:  # If no lives are left, the player loses
            game_over = True  # End the game
            print("you lose! !")  # Print a message to indicate the player lost

    # Check if all letters in the word have been guessed (i.e., no more underscores)
    if '_' not in display:  # If there are no underscores left in the display list
        game_over = True  # End the game
        print("you win! !")  # Print a message to indicate the player wonse