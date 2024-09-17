from tkinter import *

print('Flash Card Application')
BACKGROUND_COLOR = "#B1DDC6"
A_FONT = ("Arial", 40, "italic")
E_FONT = ("Arial", 60, "bold")

#my_image = PhotoImage(file="..//image_file.png")
#button = Button(image=my_image, highlightthickness=0)

window=Tk()
window.title("Flash Card Application")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canavas=Canvas(height=526,width=800,background=BACKGROUND_COLOR)
#f_image=PhotoImage("../images/card_front.png")
#b_image=PhotoImage("../images/card_back.png")
f_image=PhotoImage(file="Flash Card/images/card_front.png")
canavas.create_image(403,263,image=f_image)
canavas.create_text(400,158,text="Title",font=A_FONT)
canavas.create_text(400,263,text="word", font=E_FONT)

canavas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canavas.grid(row=0,column=0)
#title=


window.mainloop()