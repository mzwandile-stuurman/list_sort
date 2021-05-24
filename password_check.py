# password code

# tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Password checker")
root.geometry("500x500")
root.config(bg="dark slate grey")

user_label = Label(root,text="Enter user name")
user_entry = Entry(root)
user_label.place(x=10, y=10)
user_entry.place(x=150, y=10)

password_label = Label(root, text="Enter password")
password_entry = Entry(root, show="*")
password_label.place(x=10, y=100)
password_entry.place(x=150, y=100)

user_names = ["mzwandile","mambane","ingwenya","Best"]

pass_words = ["stuurman","Lengend","yibhoza","of_the_best"]
def user_pass():

    found = False
    for i in range(len(user_names)):
        if user_names[i] == user_entry.get() and pass_words[i] == password_entry.get():
            found=True
    if found == True:
        messagebox.showinfo(title=None, message= "Access granted")
        root.destroy()
        import new_form


    else:
        messagebox.showinfo(title=None, message="Access denied")



def clear():
    user_entry.delete(0,END)
    password_entry.delete(0,END)

def exit():
    root.destroy()


exit_button = Button(root, text="Exit", command=exit)
exit_button.place(x=300,y=150)

login_btn = Button(root, text="Login", command= user_pass)
login_btn.place(x=100, y=150)

clear_btn = Button(root, text="Retry", command=clear)
clear_btn.place(x=200, y=150)
root.mainloop()


