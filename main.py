from tkinter import *
from tkinter import messagebox
from prettytable import PrettyTable
import random
import pyperclip

BG_COLOR = "#17141F"
table = PrettyTable()
table.field_names = ["Website", "Email", "Password"]

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details for {website}: \nEmail: {email} \nPassword: {password} \nClick OK to continue.")

        if is_ok:
            row_only = f"| {website:<15} | {email:<25} | {password:<15} |\n"

            with open("data.txt", "a") as data_file:
                data_file.write(row_only)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(height=200, width=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="image.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", bg=BG_COLOR, fg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:", bg=BG_COLOR, fg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=BG_COLOR, fg="white")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=10)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=10)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=10)

#Buttons
generate_password_button = Button(text="Generate", width=11 ,command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add Password", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()