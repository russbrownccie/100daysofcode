from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'x', 'y', 'z']
    upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                          'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    alpha_list = [choice(lower_case_letters) for _ in range(randint(6, 8))]
    cap_alpha_list = [choice(upper_case_letters) for _ in range(randint(2, 4))]
    char_list = [choice(symbols) for _ in range(randint(2, 3))]
    num_list = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = alpha_list + cap_alpha_list + char_list + num_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_img)
canvas.grid(column=1, row=0)
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)
email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)
password_text = Label(text="Password:")
password_text.grid(column=0, row=3)
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=55)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "dudebro@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=17, command=create_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=46, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
