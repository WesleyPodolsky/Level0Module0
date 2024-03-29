from tkinter import messagebox, simpledialog, Tk
#import tkMessageBox
#tkMessageBox.showinfo(title="Greetings", message="Hello, World!")
# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    messagebox.showinfo(title="Story 1/2", message="If you find yourself having to cross a piranha-infested river, here's how to do it..." )
    # Get the player to enter an adjective
    word1 = simpledialog.askstring(title='1/5', prompt="enter an adjective")
    # Get the player to enter a type of liquid
    word2 = simpledialog.askstring(title='2/5', prompt="enter a type of liquid")
    # Get the player to enter a body part
    word3 = simpledialog.askstring(title='3/5', prompt="enter a body part")
    # Get the player to enter a verb
    word4 = simpledialog.askstring(title='4/5', prompt="enter a verb")
    # Get the player to enter a place
    word5 = simpledialog.askstring(title='5/5', prompt="enter a place")
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more " + word1 + " during the day, so cross the river at "
        "night. Piranhas are attracted to fresh " + word2 + " and will most "
        "likely take a bite out of your " + word3 + " if you " + word4 + ". Whatever "
        "you do, if you have an open wound, try to find another way to get "
        "back to the " + word5 + ". Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up
    messagebox.showinfo(title="Story 2/2", message=story)
    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

    pass
