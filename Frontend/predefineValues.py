from tkinter import *



def screenDisplay(window) :
    window.geometry("1000x700")
    window.configure(background="#ffbdbd")
    window.title("Attendance System")
    


    window.mainloop()
    # c = Canvas(width=400, height=400)
    # c.pack()

    # canvas_height =20
    # canvas_width = 30


if __name__ == "__main__":
    window = Tk()
    screenDisplay(window)
