import tkinter as tk

# Correct answers for the crossword
correct_answers = [
    ['', '', 'a','', '', 'p', ''],
    ['j', 'u', 'p', 'i', 't', 'e', 'r'],
    ['', '', 'p', '', '', 'n', ''],
    ['d', 'e', 'l', 'h', 'i', '', ''],
    ['', '', 'e', '', '', '', '']
]

def check_answers():
    
    is_correct=True
    for row in range(5):
        for column in range(7):
            entry_text = entry_grid[row][column].get().lower()
            if entry_text != correct_answers[row][column] and correct_answers[row][column] != '':
                is_correct = False
    
    result_label.config(text="Correct!" if is_correct else "Try again!")

# Create the main window
root = tk.Tk()
root.title("Crossword")

# Create a 5x7 grid of entry boxes and store them in a list
entry_grid = []

for row in range(5):
    entry_row = []
    for column in range(7):
        entry = tk.Entry(root, width=2, justify='center')
        entry.grid(row=row, column=column, padx=5, pady=5)
        entry_row.append(entry)
    entry_grid.append(entry_row)

# Blacken unused boxes based on correct_answers
for row in range(5):
    for column in range(7):
        if correct_answers[row][column] == '':
            entry_grid[row][column].config(bg='black', state='disabled', relief='flat', highlightthickness=0)


# Create a check button
check_button = tk.Button(root, text="Check", command=check_answers)
check_button.grid(row=5, column=0, columnspan=7)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=7)

# Define hints for the crossword
hints = [
    "Hints:-",
    "1. Largest planet (across)",
    "2. Capital of India (across)",
    "3. A fruit associated with newton (down)",
    "4. An object used for writing (down)"
]

# Display the hints as labels below the grid
for i, hint in enumerate(hints):
    hint_label = tk.Label(root, text=hint)
    hint_label.grid(row=7+i, column=0, columnspan=7, sticky='w', padx=5, pady=2)


# Start the main event loop
root.mainloop()
