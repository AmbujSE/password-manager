from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD PROVIDER ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data1.json", "r") as d_f:
            data = json.load(d_f)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Please make an entry first.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"These are the details:\nEmail: {email}"
                                                      f"\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No Details for The {website} website exist.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = password_letters + password_numbers + password_symbols
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = em_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left things blank")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
        #                                               f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data1.json", "r") as d_f:
                # d_f.write(f"{website} | {email} | {password}\n")
                data = json.load(d_f)
        except FileNotFoundError:
            with open("data1.json", "w") as d_f:
                json.dump(new_data, d_f, indent=4)
        else:
            data.update(new_data)

            with open("data1.json", "w") as d_f:
                json.dump(data, d_f, indent=4)
        finally:
            website_entry.delete(0, END)
            em_user_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

em_user_label = Label(text="Email/Username:")
em_user_label.grid(column=0, row=2)

em_user_entry = Entry(width=52)
em_user_entry.insert(0, string="Enter email/username name here")
em_user_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(column=2, row=3)

button2 = Button(text="Add", width=44, command=save)
button2.grid(column=1, row=4, columnspan=2)

button3 = Button(text="Search", width=14, command=find_password)
button3.grid(column=2, row=1)

window.mainloop()
