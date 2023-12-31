from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {
            "email": username,
            "password": password,

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty")

    else:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username}\nPassword: "
                                               f"{password} \nIs it ok to save")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump(data_dict, file, indent=4)
            else:
                data.update(data_dict)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            messagebox.showinfo(title="Success", message="Password Saved successfully")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    account = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title='oops', message="No datafile found")
    else:
        if account in data:
            username = data[account]["email"]
            password = data[account]["password"]
            messagebox.showinfo(title="Result", message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title='oops', message=f"No details for {account} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(width=14)
search_button.config(text="Search", command=find_password)
search_button.grid(row=1, column=2)

username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "rajhemant760@gmail.com")

password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(width=44)
add_button.config(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
