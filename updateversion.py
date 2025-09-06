import tkinter as tk
import random

# Game options
options = ["Rock", "Paper", "Scissors"]

# Initialize scores
player_score = 0
computer_score = 0

def play(choice):
    global player_score, computer_score
    
    # Get computer's choice
    computer_choice = random.choice(options)
    
    # Update labels
    player_label.config(text=f"Player: {choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    # Determine winner
    if choice == computer_choice:
        result_label.config(text="It's a Draw!", fg="blue")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win! 🎉", fg="green")
        player_score += 1
    else:
        result_label.config(text="Computer Wins! 😢", fg="red")
        computer_score += 1
    
    # Update scores
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Player: 0  |  Computer: 0")
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Let's Play!", fg="black")

# Create window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.config(bg="#f4f4f4")

# Labels
title_label = tk.Label(root, text="Rock-Paper-Scissors 🎮", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

player_label = tk.Label(root, text="Player: ", font=("Arial", 12), bg="#f4f4f4")
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12), bg="#f4f4f4")
computer_label.pack()

result_label = tk.Label(root, text="Let's Play!", font=("Arial", 14, "bold"), bg="#f4f4f4")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Player: 0  |  Computer: 0", font=("Arial", 12, "bold"), bg="#f4f4f4")
score_label.pack(pady=5)

# Buttons for choices
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock 🪨", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper 📄", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors ✂️", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Reset & Exit Buttons
reset_btn = tk.Button(root, text="Reset Game", width=12, command=reset_game)
reset_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", width=12, command=root.quit)
exit_btn.pack(pady=5)

root.mainloop()
