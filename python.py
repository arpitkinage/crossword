import tkinter as tk
import random

# Correct answers for the crossword
correct_answers = [
    ['', '', 'a', '', '', 'p', ''],
    ['j', 'u', 'p', 'i', 't', 'e', 'r'],
    ['', '', 'p', '', '', 'n', ''],
    ['d', 'e', 'l', 'h', 'i', '', ''],
    ['', '', 'e', '', '', '', '']
]


# Clue letters to be pre-filled in the grid (using a dictionary instead of a list)
clue_letters = {
    (0, 2): 'A',
    (1, 0): 'J',
    (1, 5): 'E',
    (1, 6): 'R',
    (3, 0): 'D',
    (3, 3): 'H',
    (3, 4): 'I',
    (4, 2): 'E',
}


def check_answers():
    is_correct = True
    for row in range(5):
        for column in range(7):
            entry_text = entry_grid[row][column].get().lower()
            if entry_text != correct_answers[row][column] and correct_answers[row][column] != '':
                is_correct = False
    
    result_label.config(text="Correct!" if is_correct else "Try again!")

def reveal_answers():
    for row in range(5):
        for column in range(7):
            if correct_answers[row][column] != '':
                entry_grid[row][column].delete(0, tk.END)  # Clear the box
                entry_grid[row][column].insert(0, correct_answers[row][column].upper())
                entry_grid[row][column].config(state='disabled', fg='green')

def reveal_word_1():
    word_1 = ['j', 'u', 'p', 'i', 't', 'e', 'r']  # Word for hint 1: Largest planet
    for i, letter in enumerate(word_1):
        entry_grid[1][i].delete(0, tk.END)  # Clear the box
        entry_grid[1][i].insert(0, letter.upper())
        entry_grid[1][i].config(state='disabled', fg='green')

def reveal_word_2():
    word_2 = ['d', 'e', 'l', 'h', 'i']  # Word for hint 2: Capital of India
    for i, letter in enumerate(word_2):
        entry_grid[3][i].delete(0, tk.END)  # Clear the box
        entry_grid[3][i].insert(0, letter.upper())
        entry_grid[3][i].config(state='disabled', fg='green')

def reveal_word_3():
    word_3 = ['a', 'p', 'p', 'l', 'e']  # Word for hint 3: A fruit associated with Newton (down)
    for i, letter in enumerate(word_3):
        entry_grid[i][2].delete(0, tk.END)  # Clear the box
        entry_grid[i][2].insert(0, letter.upper())
        entry_grid[i][2].config(state='disabled', fg='green')

def reveal_word_4():
    word_4 = ['p', 'e', 'n']  # Word for hint 4: An object used for writing (down)
    for i, letter in enumerate(word_4):
        entry_grid[i][5].delete(0, tk.END)  # Clear the box
        entry_grid[i][5].insert(0, letter.upper())
        entry_grid[i][5].config(state='disabled', fg='green')

# Create the main window
root = tk.Tk()
root.title("Crossword")

# Create a 5x7 grid of entry boxes and store them in a list
entry_grid = []

for row in range(5):
    entry_row = []
    for column in range(7):
        entry = tk.Entry(root, width=4, justify='center')
        entry.grid(row=row, column=column, padx=15, pady=15)
        entry_row.append(entry)
    entry_grid.append(entry_row)
    
# Pre-fill clue letters in the grid
for (row, col), letter in clue_letters.items():
    entry_grid[row][col].insert(0, letter)
    entry_grid[row][col].config(state='disabled', fg='blue')

# Blacken unused boxes based on correct_answers
for row in range(5):
    for column in range(7):
        if correct_answers[row][column] == '':
            entry_grid[row][column].config(bg='black', state='disabled', relief='flat', highlightthickness=0)

# Create a check button
check_button = tk.Button(root, text="Check", command=check_answers)
check_button.grid(row=5, column=0, columnspan=3)

# Create a reveal button with the updated title
reveal_button = tk.Button(root, text="Reveal All Answers", command=reveal_answers)
reveal_button.grid(row=5, column=4, columnspan=3)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=7)

# Define hints for the crossword
hints = [
    "Hints:-",
    "1. Largest planet (across)",
    "2. Capital of India (across)",
    "3. A fruit associated with Newton (down)",
    "4. An object used for writing (down)"
]

# Display the hints as labels 
for i, hint in enumerate(hints[1:], start=1):
    hint_label = tk.Label(root, text=hint)
    hint_label.grid(row=6 + i, column=0, columnspan=6, sticky='w', padx=5, pady=2)

# Add reveal buttons next to each hint
reveal_button_1 = tk.Button(root, text="Reveal", command=reveal_word_1)
reveal_button_1.grid(row=7, column=6)

reveal_button_2 = tk.Button(root, text="Reveal", command=reveal_word_2)
reveal_button_2.grid(row=8, column=6)

reveal_button_3 = tk.Button(root, text="Reveal", command=reveal_word_3)
reveal_button_3.grid(row=9, column=6)

reveal_button_4 = tk.Button(root, text="Reveal", command=reveal_word_4)
reveal_button_4.grid(row=10, column=6)

# List of possible button texts
reveal_button_texts = ["Reveal", "Show Answer", "Unveil", "Solution"]

# Randomly choose one text for all reveal buttons
random_text = random.choice(reveal_button_texts)

# Set the same text for all reveal buttons
reveal_button_1.config(text=random_text)
reveal_button_2.config(text=random_text)
reveal_button_3.config(text=random_text)
reveal_button_4.config(text=random_text)

# Start the main event loop
root.mainloop()

