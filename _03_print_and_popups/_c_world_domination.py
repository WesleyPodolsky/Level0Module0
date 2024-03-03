from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window=Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Ask the user if they know how to write code.
answer = messagebox.askquestion(title="???", message="do you know how to write code")
messagebox.showinfo(title = "!!!", message=answer + "?")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
if answer == "yes":
    messagebox.showinfo(title = "!!!", message="you will rule the world")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
elif answer != "yes":
    messagebox.showerror(title="...", message="sign up for classes at The League")
    # Run the window's .mainloop() method
window.mainloop()
