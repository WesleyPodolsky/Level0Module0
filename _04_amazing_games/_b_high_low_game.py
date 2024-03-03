from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
#print(random_num) commented b/c didn't want to know nu,ber while i play
    # 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):

        # 4. Ask the user for a guess using a pop-up window, and save their response
    lastGuess = simpledialog.askstring(title=str(i) + '/10', prompt="guess a number 1-100")
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
    if int(lastGuess) == random_num:
        messagebox.showinfo(title = "huh", message="u win")
        sys.exit(0)
        # 7. if the guess is high
            # 8. Tell them it's too high
    elif int(lastGuess) > random_num:
        messagebox.showinfo(title = 'huh', message="Lower")


        # 9. Else if the guess is low
            # 10. Tell them it's too low
    elif int(lastGuess) < random_num:
        messagebox.showinfo(title = "!!!", message="Higher")
    #11. Outside of the loop, tell the user they lost
messagebox.showinfo(title = "!!!", message="you lost L")
window.mainloop()
