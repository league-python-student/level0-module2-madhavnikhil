import tkinter as tk
from tkinter import simpledialog, Tk, messagebox
from PIL import Image, ImageTk

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    Animal = simpledialog.askstring(title=window, prompt="Which animal do you want?")

    # TODO 2. Make it so that the user can keep entering new animals.
    while (Animal != "exit"):
        if Animal == "Cow":
            moo()
        if Animal == "Duck":
            quack()
        if Animal == "Dog":
            woof()
        if Animal == "Cat":
            meow()
        if Animal == "Llama":
            llama_scream()
        Animal = simpledialog.askstring(title=window, prompt="Which animal do you want?")
    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    show_image('cow.jpg')
    messagebox.showinfo(title=window, message="Moo")


def quack():
    show_image('duck.jpg')
    messagebox.showinfo(title=window, message="Quack")


def woof():
    show_image('dog.jpg')
    messagebox.showinfo(title=window, message="Woof")


def meow():
    show_image('cat.jpg')
    messagebox.showinfo(title=window, message="Meow")



def llama_scream():
    show_image('llama.jpg')



if __name__ == '__main__':
    animals()
