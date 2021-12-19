from tkinter import *



def screenDisplay(window) :
    window.geometry("1000x700")
    window.configure(background="#ffbdbd")
    window.title("Attendance System")
    
    window.mainloop()
    


if __name__ == "__main__":
    window = Tk()
    screenDisplay(window)
