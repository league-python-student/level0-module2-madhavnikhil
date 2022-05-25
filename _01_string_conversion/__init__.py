from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = 5
    messagebox.showinfo(None, str(num1))

