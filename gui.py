from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Yadav Motor's")
root.iconbitmap("pixel3.ico")

# Full screen
root.state("zoomed")

# Screen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# -------- Background Image --------
bg_img = Image.open("background.jpg")
bg_img = bg_img.resize((width, height))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

# -------- Login Frame --------
frame = Frame(root, bg="white", bd=5, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=420, height=480)

# -------- Logo --------
img = Image.open("star.png")
resize_img = img.resize((120,80))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(frame, image=img, bg="white")
img_label.pack(pady=10)

# -------- Title --------
title = Label(frame, text="Yadav Motor's",
              font=("Arial",24,"bold"), bg="white", fg="black")
title.pack(pady=5)

# -------- Email --------
email_label = Label(frame, text="Email",
                    font=("Arial",14,"bold"), bg="white")
email_label.pack(pady=(20,5))

email_entry = Entry(frame, font=("Arial",14), width=25,
                    bd=2, relief=SOLID)
email_entry.pack(pady=5)

# -------- Password --------
password_label = Label(frame, text="Password",
                       font=("Arial",14,"bold"), bg="white")
password_label.pack(pady=(20,5))

password_entry = Entry(frame, font=("Arial",14), show="*",
                       width=25, bd=2, relief=SOLID)
password_entry.pack(pady=5)

# -------- Login Button --------
login_btn = Button(frame, text="Login",
                   font=("Arial",14,"bold"),
                   bg="#FFA500", fg="white",
                   width=15, height=1)
login_btn.pack(pady=30)

root.mainloop()