from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pswd():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    number=['0','1','2','3','4','5','6','7','8','9']
    symbol=['!','#','$','%','&','+','*']
    l=random.randint(8,18)
    sy=random.randint(2,4)
    num=random.randint(2,4)

    p_letter=[random.choice(letters) for _ in range(l) ]
    p_symbol=[random.choice(symbol) for _ in range(sy)]
    p_number=[random.choice(number) for _ in range(num)]

    p_list=p_letter+p_symbol+p_number
    random.shuffle(p_list)
    p="".join(p_list)
    pswd_entry.insert(0,p)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web=l1_entry.get()
    email=email_entry.get() 
    pswd=pswd_entry.get()

    if len(web)==0 or len(pswd)==0:
        messagebox.showinfo(title="Oops...", message="Please make sure you haven't left any fields empty")
    else:
        #messagebox.showinfo(title="Title", message="message")
        msg=messagebox.askokcancel( title=web, message=f"These are the details entered :\nEmail: {email}\n Password: {pswd}\nIs it ok to save?")
        if msg:
            with open("data.txt","a") as data_file:
                data_file.write(f"{web} | {email} | {pswd}\n")
                l1_entry.delete(0,END)
                email_entry.insert(0,"xyz@abc.com")
                pswd_entry.delete(0,END)

        

    



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password manager")
window.config(padx=60,pady=60)

canvas=Canvas(height=200, width=200)
logo_image=PhotoImage(file="C:\\Users\\nikit\\OneDrive\\Desktop\\Python\\logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

l1=Label(text="Website:")
l1.grid(row=1,column=0)
email=Label(text="Email/Username:")
email.grid(row=2,column=0)
pswd=Label(text="Password")
pswd.grid(row=3, column=0)

#Entries
l1_entry=Entry(width=35)
l1_entry.grid(row=1,column=1,columnspan=2)
l1_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"xyz@abc.com") 
pswd_entry=Entry(width=35)
pswd_entry.grid(row=3,column=1,columnspan=2)

#Button
g_pswd_button=Button(text="Generate Password",command=generate_pswd)
g_pswd_button.grid(row=3,column=2)
add_button=Button(text="Add", width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()