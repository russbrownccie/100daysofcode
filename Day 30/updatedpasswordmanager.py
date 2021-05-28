
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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
    new_data={
        website: {
            "email":email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")

    else:
        try:
            with open("data.json", "r",) as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r", ) as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title=website, message="No details for the website exist")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")

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
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1,)
website_entry.focus()
user_entry = Entry(width=55)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "dudebro@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=17, command=create_password)
password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=17, command=find_password)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=52, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
