import random
import tkinter as tk
import tkinter
from tkinter import messagebox

class Game:
    def __ini__(self):
        self.scissor
        self.rock
        self.paper
        self.lizard
        self.spock
        self.your_score
        self.oponent_score
        self.comp

top = tk.Tk()
top.title("Rock -> Paper -> Scissor -> Lizard -> Spock")

Game.rock = tk.PhotoImage(file="./images/rock.png")
Game.paper = tk.PhotoImage(file="./images/paper.png")
Game.scissor = tk.PhotoImage(file="./images/scissor.png")
Game.lizard = tk.PhotoImage(file="./images/lizard.png")
Game.spock = tk.PhotoImage(file="./images/spock.png")

Game.oponent_score = 0
Game.your_score = 0

def Rock():
    Game.comp = random.randint(1, 5)
    if Game.comp == 3:
        Game.comp = "Scissors"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nRock crush Scissors \n"
            + "Your Choice:Rock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 1:
        Game.comp = "Rock"
        messagebox.showinfo(
            "You made Same choice!",
            "EQUALITY!\n"
            + "Your Choice:Rock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 2:
        Game.comp = "Lizard"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nRock crush Lizard \n"
            + "Your Choice:Rock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nSpock vaporize Rock \n"
            + "Your Choice:Rock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    else:
        Game.comp = "Paper"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nPaper covers Rock \n"
            + "Your Choice:Rock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )


def paper():
    Game.comp = random.randint(1, 5)
    if Game.comp == 1:
        Game.comp = "Rock"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nPaper covers Rock \n"
            + "Your Choice: Paper\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 2:
        Game.comp = "Paper"
        messagebox.showinfo(
            "You made Same choice!",
            "EQUALITY!\n"
            + "Your Choice: Paper\n"
            + "\nOponent's Choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 3:
        Game.comp = "Lizard"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nLizard eats Paper\n"
            + "Your Choice: Paper\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nPaper discards Spock \n"
            + "Your Choice: Paper\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    else:
        Game.comp = "Scissors"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nScissors cut Paper \n"
            + "Your Choice: Paper\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )


def scissors():
    Game.comp = random.randint(1, 5)
    if Game.comp == 2:
        Game.comp = "Paper"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nScissors cut Paper \nYour Choice: Scissors\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        messagebox.showinfo(
            "You made Same choice!",
            "EQUALITY!\nYour Choice: Scissors\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nScissors descapitates Lizard \n"
            + "Your Choice:Scissors\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nSpock smash Scissors \n"
            + "Your Choice:Scissors\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    else:
        Game.comp = "Rock"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nRock crush Scissors \nYour Choice: Scissors\n"
            + "\nOponent's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )


def lizard():
    Game.comp = random.randint(1, 5)
    if Game.comp == 2:
        Game.comp = "Paper"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nLizard eats Paper \nYour Choice: Lizard\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU have LOST!\nScissors descapitates Lizard \nYour Choice: Lizard\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        messagebox.showinfo(
            "You made Same choice!",
            "EQUALITY!\n"
            + "Your Choice: Lizard\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nLizard poison Spock \n"
            + "Your Choice:Lizard\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    else:
        Game.comp = "Rock"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nRock crush Lizard \nYour Choice: Lizard\n"
            + "\nOponent's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )


def spock():
    Game.comp = random.randint(1, 5)

    if Game.comp == 2:
        Game.comp = "Paper"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU LOST!\nPaper discards Spock \nYour Choice: Spock\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN !\nSpock smash Scissors \nYour Choice: Spock\n"
            + "\nOponent's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        Game.oponent_score += 1
        messagebox.showinfo(
            " You are unlucky!",
            "YOU have LOST!\nLizard poison Spock \n"
            + "Your Choice: Spock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        messagebox.showinfo(
            "You made Same choice!",
            "EQUALITY!\n"
            + "Your Choice: Spock\n"
            + "\nOponent's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )

    else:
        Game.comp = "Rock"
        Game.your_score += 1
        messagebox.showinfo(
            "Congrats!",
            "YOU have WIN!\nSpock vaporize Rock \nYour Choice: Spock\n"
            + "\nOponent's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.your_score)
            + "\nOponent's Score: "
            + str(Game.oponent_score),
        )


But1 = tkinter.Button(
    top, image=Game.rock, height="150", width="150", command=Rock
)
But2 = tkinter.Button(
    top, image=Game.paper, height="150", width="150", command=paper
)
But3 = tkinter.Button(
    top, image=Game.scissor, height="150", width="150", command=scissors
)
But4 = tkinter.Button(
    top, image=Game.lizard, height="150", width="150", command=lizard
)
But5 = tkinter.Button(
    top, image=Game.spock, height="150", width="150", command=spock
)

But1.pack(side="left")
But2.pack(side="left")
But3.pack(side="left")
But4.pack(side="left")
But5.pack(side="left")

top.mainloop()
