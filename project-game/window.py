from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
def d():
   print('h')
def main():
    global window
    window.destroy()
    window1 = Tk()
    window1.title('ba')
    window1.geometry(f'{app_width}x{app_height}')
    frame = Frame(window1, width=app_width, height=app_height)
    frame.pack()
    canvas=Canvas(frame,width=app_width, height=app_height)
    canvas.pack()
    # creat_button=Button(frame,command=d,bg='blue',width=100,height=10)
    # creat_button.pack()
    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width,app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0,0,image=background,anchor=NW)
    window1.mainloop()
    
window = Tk()
app_width = window.winfo_screenwidth()
app_height = window.winfo_screenheight()
window.geometry(f'{app_width}x{app_height}')
bg_image = Image.open("./image/Premium Vector _ Mountains and bright sky in the morning_.jfif")
bg_image = bg_image.resize((app_width,app_height))
background = ImageTk.PhotoImage(bg_image)

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor=NW)

Player = Image.open("./image/Mario.png")
Player = Player.resize((140, 145)) 
Player = ImageTk.PhotoImage(Player)
Player_image = canvas.create_image(150, 527, image=Player, anchor=CENTER)

Coins1 = Image.open("./image/Coins11.png")
Coins1 = Coins1.resize((50, 40)) 
Coins1 = ImageTk.PhotoImage(Coins1)
Coins_img = canvas.create_image(230, 550, image=Coins1, anchor=CENTER)

Coins2 = Image.open("./image/Coins11.png")
Coins2 = Coins2.resize((50, 40)) 
Coins2 = ImageTk.PhotoImage(Coins2)
Coins_img = canvas.create_image(260, 550, image=Coins2, anchor=CENTER)

Coins3 = Image.open("./image/Coins11.png")
Coins3 = Coins3.resize((50, 40)) 
Coins3 = ImageTk.PhotoImage(Coins3)
Coins_img = canvas.create_image(290, 550, image=Coins3, anchor=CENTER)

Coins4 = Image.open("./image/Coins11.png")
Coins4 = Coins4.resize((50, 40)) 
Coins4 = ImageTk.PhotoImage(Coins4)
Coins_img = canvas.create_image(230, 570, image=Coins4, anchor=CENTER)

Coins5 = Image.open("./image/Coins11.png")
Coins5 = Coins5.resize((50, 40)) 
Coins5 = ImageTk.PhotoImage(Coins5)
Coins_img = canvas.create_image(260, 570, image=Coins5, anchor=CENTER)

Coins6 = Image.open("./image/Coins11.png")
Coins6 = Coins6.resize((50, 40)) 
Coins6 = ImageTk.PhotoImage(Coins6)
Coins_img = canvas.create_image(280, 570, image=Coins6, anchor=CENTER)

Coins7 = Image.open("./image/Coins11.png")
Coins7 = Coins7.resize((50, 40)) 
Coins7 = ImageTk.PhotoImage(Coins7)
Coins_img = canvas.create_image(300, 570, image=Coins7, anchor=CENTER)

Coins8 = Image.open("./image/Coins11.png")
Coins8 = Coins8.resize((50, 40)) 
Coins8 = ImageTk.PhotoImage(Coins8)
Coins_img = canvas.create_image(320, 570, image=Coins8, anchor=CENTER)

Coins9 = Image.open("./image/Coins11.png")
Coins9 = Coins9.resize((50, 40)) 
Coins9 = ImageTk.PhotoImage(Coins9)
Coins_img = canvas.create_image(315, 550, image=Coins9, anchor=CENTER)
Coins10 = Image.open("./image/Coins11.png")
Coins10 = Coins10.resize((50, 40)) 
Coins10 = ImageTk.PhotoImage(Coins10)
Coins_img = canvas.create_image(335, 560, image=Coins10, anchor=CENTER)

splash_label = Label(window, text="Power A-five", font=("Robus", 60, "bold"))
splash_label.pack()
splash_label.place(relx=0.5, rely=0.3, anchor='center')

window.title("Progress Bar in Tk")
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=170, y=390, width=240)
progressbar.start()

window.after(1000, main)
window.mainloop()