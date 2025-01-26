import tkinter as tk
import random
root = tk.Tk()
root.title("CROSSWORD")

# Correct answers for the crossword
answers = [
    ['', '', 'A', '', '', 'P', ''],
    ['J', 'U', 'P', 'I', 'T', 'E', 'R'],
    ['', '', 'P', '', '', 'N', ''],
    ['D', 'E', 'L', 'H', 'I', '', ''],
    ['', '', 'E', '', '', '', '']
]

# Define hints for the crossword
hints = [
    "Hints:-",
    "1. Largest planet (across)",
    "2. Capital of India (across)",
    "3. A fruit associated with Newton (down)",
    "4. An object used for writing (down)"
]
 
row = 7 
for i in hints:
    tk.Label(root, text=i).grid(row=row, column=0, columnspan=6, padx=5, pady=2, sticky='w')
    row += 1 

# Clue letters to be pre-filled in the grid 
clues = {
    (0, 2): 'A',
    (1, 0): 'J',
    (1, 5): 'E',
    (1, 6): 'R',
    (3, 0): 'D',
    (3, 4): 'I',
    (4, 2): 'E',
}

# Create a 5x7 grid of entry boxes
grid = []

for row in range(5):
    entry_row = []
    for column in range(7):
        entry = tk.Entry(root, width=4, justify='center')
        entry.grid(row=row, column=column, padx=15, pady=15)
        entry_row.append(entry)
    grid.append(entry_row)
    
# Pre-fill clue letters in the grid
for (row, col), letter in clues.items():
    grid[row][col].insert(0, letter)
    grid[row][col].config(state='disabled')

# Disable unused boxes
for row in range(5):
    for column in range(7):
        if answers[row][column] == '':
            grid[row][column].config(state='disabled', relief='flat')
            
# Create a label to display the result
result = tk.Label(root, text="")
result.grid(row=6, column=0, columnspan=7)

def checkanswers():
    correct = True
    for row in range(5):
        for column in range(7):
            userinput = grid[row][column].get().upper()
            if userinput != answers[row][column] and answers[row][column] != '':
                correct = False
    result.config(text="Your answer is correct!" if correct else "Your answer is wrong. Try again")

def revealall():
    for row in range(5):
        for column in range(7):
            if answers[row][column] != '':
                grid[row][column].delete(0, tk.END)  
                grid[row][column].insert(0, answers[row][column].upper())
                grid[row][column].config(state='disabled')

def reveal1():
    word1 = ['J', 'U', 'P', 'I', 'T', 'E', 'R']
    for i in range(7):
        grid[1][i].delete(0, tk.END)
        grid[1][i].insert(0, word1[i])
        grid[1][i].config(state='disabled')

def reveal2():
    word2 = ['D', 'E', 'L', 'H', 'I']
    for i in range(5):
        grid[3][i].delete(0, tk.END)
        grid[3][i].insert(0, word2[i])
        grid[3][i].config(state='disabled')

def reveal3():
    word3 = ['A', 'P', 'P', 'L', 'E']
    for i in range(5):
        grid[i][2].delete(0, tk.END)
        grid[i][2].insert(0, word3[i])
        grid[i][2].config(state='disabled')

def reveal4():
    word4 = ['P', 'E', 'N']
    for i in range(3):
        grid[i][5].delete(0, tk.END)
        grid[i][5].insert(0, word4[i])
        grid[i][5].config(state='disabled')

# Create reveal buttons for hints
revealallbutton = tk.Button(root, text="Reveal All Answers", command=revealall)
revealallbutton.grid(row=5, column=4, columnspan=3)

revealbutton1 = tk.Button(root, text="Reveal", command=reveal1)
revealbutton1.grid(row=8, column=6)

revealbutton2 = tk.Button(root, text="Reveal", command=reveal2)
revealbutton2.grid(row=9, column=6)

revealbutton3 = tk.Button(root, text="Reveal", command=reveal3)
revealbutton3.grid(row=10, column=6)

revealbutton4 = tk.Button(root, text="Reveal", command=reveal4)
revealbutton4.grid(row=11, column=6)

# Randomly choose one text for all reveal buttons
revealtext = ["Reveal", "Show Answer", "Unveil", "Solution"]
randomtext = random.choice(revealtext)
revealbutton1.config(text=randomtext)
revealbutton2.config(text=randomtext)
revealbutton3.config(text=randomtext)
revealbutton4.config(text=randomtext)

# Create a submit button
submit = tk.Button(root, text="Submit", command=checkanswers)
submit.grid(row=5, column=0, columnspan=3)

root.mainloop()
