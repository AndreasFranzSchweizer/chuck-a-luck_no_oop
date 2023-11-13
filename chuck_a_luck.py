import tkinter as tk
from tkinter import messagebox
import random

bet = 0
chosen_number = 1
dice_results = None

def roll_dice():
    global dice_results
    dice_results = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

def check_result():
    return chosen_number in dice_results

def show_info(message):
    messagebox.showinfo("Ergebnis", message)

def show_error(message):
    messagebox.showerror("Fehler", message)

def show_result(bet):
    result = "Die Würfel zeigen: {}, {}, {}".format(*dice_results)

    if check_result():
        show_info("Glückwunsch! Du hast gewonnen {} Einheiten.".format(bet))
    else:
        show_info("Leider verloren. Du verlierst deinen Einsatz.")

def handle_roll():
    global bet, chosen_number
    try:
        bet = int(bet_entry.get())
        chosen_number = int(number_entry.get())
    except ValueError:
        show_error("Ungültige Eingabe. Bitte geben Sie ganze Zahlen ein.")
        return

    roll_dice()
    show_result(bet)

# GUI
root = tk.Tk()
root.title("Chuck-a-Luck")

label = tk.Label(root, text="Willkommen bei Chuck-a-Luck!")
label.pack()

bet_label = tk.Label(root, text="Einsatz:")
bet_label.pack()

bet_entry = tk.Entry(root, width=10)
bet_entry.pack()

number_label = tk.Label(root, text="Gewählte Zahl:")
number_label.pack()

number_entry = tk.Entry(root, width=10)
number_entry.pack()

roll_button = tk.Button(root, text="Würfeln", command=handle_roll)
roll_button.pack()

root.mainloop()
