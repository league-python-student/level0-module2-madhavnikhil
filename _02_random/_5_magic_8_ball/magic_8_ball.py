import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    randy = random.randint(0, 3)
    # If the random number is 0
Nickel = simpledialog.askstring(title=window, prompt="Enter in a question.")
if randy == 0:
    messagebox.showinfo(title=window, message="Yes")
        # tell the user "Yes"

    # If the random number is 1
elif randy == 1:
    messagebox.showinfo(title=window, message="No")
        # tell the user "No"

    # If the random number is 2
elif randy == 2:
    messagebox.showinfo(title=window, message="Maybe you should ask google.")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
elif randy == 3:
    messagebox.showinfo(title=window, message="Yes it is")
        # write your own answer
