from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
#PASSWORD GENERATOR:
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_for_password.insert(0, password)
    pyperclip.copy(password)


#SAVE PASSWORD
def write():
    website = entry_for_website.get()
    mail = entry_for_email.get()
    password = entry_for_password.get()
    if len(website) == 0 or len(password) == 0 or len(mail) == 0:
        messagebox.showerror(title="Oops", message="You left some field's empty")
    else:
        is_okay = messagebox.askokcancel(title=f"Website name= {entry_for_website.get()}",
                               message=f"These are the details: \nEmail: {mail} "
                                         f"\nPassword: {password}"
                                         f"\n Is it okay to save?")

        if is_okay:
            with open("password.txt", mode="a") as file:
                file.write(f"{website}   |    {email}     |    {password} \n")
                entry_for_website.delete(0, END)
                entry_for_password.delete(0, END)



# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

entry_for_website = Entry(width=34)
entry_for_website.grid(column=1, row=1, columnspan=2)
entry_for_website.focus()

entry_for_email = Entry(width=34)
entry_for_email.grid(column=1, row=2, columnspan=2)
entry_for_email.insert(END, "email@.com")

entry_for_password = Entry(width=17)
entry_for_password.grid(column=1, row=3,)

pass_button = Button(text="Generate Password", justify="left", command=generate)
pass_button.grid(column=2, row=3, sticky="E")

add_button = Button(text="Add", width=30, command=write)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
