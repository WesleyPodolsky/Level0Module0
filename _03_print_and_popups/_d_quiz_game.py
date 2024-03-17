from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

#if __name__ = '__main__':
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
userScore = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
lastAnswer = simpledialog.askstring(title="MATH", prompt="What is the square of 9?")
    #      // 3.  Use an if statement to check if their answer is correct
if lastAnswer == "81":
    userScore  = userScore+1
    #      // 4.  if the user's answer was correct, add one to their score 
elif lastAnswer != "81":
    userScore = userScore -1
#************************************************************************
#************************************************************************
#************************************************************************

lastAnswer = simpledialog.askstring(title="MATH", prompt="What is the square of 16?")
#      // 3.  Use an if statement to check if their answer is correct
if lastAnswer == "256":
    userScore = userScore + 1
    #      // 4.  if the user's answer was correct, add one to their score
elif lastAnswer != "256":
    userScore = userScore - 1
#************************************************************************
#************************************************************************
#************************************************************************

lastAnswer = simpledialog.askstring(title="MATH", prompt="What is the square of 100?")
#      // 3.  Use an if statement to check if their answer is correct
if lastAnswer == "10000" or lastAnswer == "10,000" :
    userScore = userScore + 1
        #      // 4.  if the user's answer was correct, add one to their score
elif lastAnswer != "10000" or lastAnswer != "10,000":
    userScore = userScore - 1
# After all the questions have been asked, tell the user their final score
# remember to convert your variable to a string using the str() function
messagebox.showinfo(title="FINAL SCORE", message='your score is ' + str(userScore))
    # Run the window's .mainloop() method
window.mainloop()