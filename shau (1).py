import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(i, j):
    if board[i][j] == "":
        board[i][j] = current_player.get()
        buttons[i][j].config(text=current_player.get())
        
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player.get()} wins!")
            reset_game()
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player.set("O" if current_player.get() == "X" else "X")

# Function to check if there's a winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to reset the game
def reset_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
    current_player.set("X")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize board and current player
board = [["" for _ in range(3)] for _ in range(3)]
current_player = tk.StringVar(value="X")

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, font=('normal', 20), 
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Start the game
root.mainloop()
