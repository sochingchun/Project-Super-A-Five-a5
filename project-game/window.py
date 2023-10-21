from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def main():
    global window
    window.destroy()
    window = Tk()
    window.title('ab')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree2.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    canvas.create_text(650, 170, text="Super A Five", fill="blue", font=('DRAGON HUNTER', 50))

    def button_clicked():
        print("Button clicked!")
    button_back = Button(canvas, text="Setting",font=90, command=button_clicked, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=250, width=250)
    
    button_back2 = Button(canvas, text="Menu",font=90 ,command=button_clicked, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=370, width=250)

    button_back3 = Button(canvas, text="Start Game",font=90, command=button_clicked, bg='blue',border=25)
    button_back3.pack()
    button_back3.place(x=550, y=490, width=250)

    window.after(3000, window3)
    window.mainloop()

def window3():
    global window
    window.destroy() 
    window = Tk()
    window.title('av')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    def button_clicked():
        print("Button clicked!")
    button_back = Button(canvas, text="Back",font=40, command=button_clicked, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    button_back = Button(canvas, text="Hard",font=90, command=button_clicked, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=220, width=250)
    
    button_back2 = Button(canvas, text="Normal",font=90, command=button_clicked, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=340, width=250)

    button_back3 = Button(canvas, text="Easy",font=90, command=button_clicked, bg='blue',border=25)
    button_back3.pack()
    button_back3.place(x=550, y=460, width=250)
    window.after(1000, window4)
    window.mainloop()


def window4():
    global window
    window.destroy() 
    windows4 = Tk()
    windows4.title('v')
    app_width = windows4.winfo_screenwidth()
    app_height = windows4.winfo_screenheight()
    windows4.geometry(f'{app_width}x{app_height}')
    frame = Frame(windows4, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/window4.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)

    #    ------Wall------    
    canvas.create_rectangle(0, 630, 400, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
    canvas.create_rectangle(500, 630, 1536, 810, fill="black", tags="wall")
    canvas.create_rectangle(500, 530, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(600, 570, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(650, 595, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 530, 350, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 570, 300, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 600, 250, 810, fill="black", tags="wall")
#
    windows4.mainloop()

window = Tk()
app_width = window.winfo_screenwidth()
app_height = window.winfo_screenheight()
window.geometry(f'{app_width}x{app_height}')
bg_image = Image.open("./image/window1.png")
bg_image = bg_image.resize((app_width, app_height))
background = ImageTk.PhotoImage(bg_image)

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor=NW)

splash_label = Label(window, text="Power A-five", font=("Robus", 60, "bold"))
splash_label.pack()
splash_label.place(relx=0.5, rely=0.3, anchor='center')

window.title("Progress Bar in Tk")
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=550, y=390, width=240)
progressbar.start()
window.after(2000, main) 


window.mainloop()
