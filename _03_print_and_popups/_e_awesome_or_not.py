from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
numberOne = random.randint(0, 3)
    # 2. Print your variable to the console
print(numberOne)
    # 3. Get the user to enter something that they think is awesome
smthAwe = simpledialog.askstring(title="???", prompt="enter something awesome")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
if numberOne == 0:
    messagebox.showinfo(title="!!!", message= smthAwe + " is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
if numberOne == 1:
    messagebox.showinfo(title="!!!", message= smthAwe + " is ok!")

    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
if numberOne == 2:
    messagebox.showinfo(title="!!!", message= smthAwe + " is boring!")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
if numberOne == 3:
    messagebox.showinfo(title="!!!", message= smthAwe + " is the most awful thing ever!")
    # Run the window's .mainloop() method
window.mainloop()
