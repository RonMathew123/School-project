import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import smtplib
from email.message import EmailMessage
import imghdr
import qrcode
from tkinter import Tk, Entry, Button, Label, StringVar, OptionMenu, messagebox, filedialog
from PIL import Image, ImageTk

def check():
    username_check="Ron"
    password_check="ty"
    username1=username.get()
    password1=password.get()
    if username1==username_check and password1==password_check:
        login.destroy()
        def generate_qr_code():
            gmail1=Ent.get()
            student_name = student_name_entry.get()
            father_name = father_name_entry.get()
            mother_name = mother_name_entry.get()
            selected_class = class_var.get()
            selected_section = section_var.get()

    
            if not (student_name and father_name and mother_name and selected_class and selected_section and gmail1):
                messagebox.showwarning("Incomplete Information", "Please fill all fields.")
                return

    
            qr_data = f"Student Name: {student_name}\nFather's Name: {father_name}\nMother's Name: {mother_name}\nClass: {selected_class}\nSection: {selected_section}"

    
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

    
            qr_img = qr.make_image(fill="black", back_color="white")

    
            qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
            qr_img_tk = ImageTk.PhotoImage(qr_img)
            qr_label.config(image=qr_img_tk)
            qr_label.image = qr_img_tk

    
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                qr_img.save(save_path)
                messagebox.showinfo("QR Code Saved", f"QR code saved to {save_path}")
            b="ronmathew2007@gmail.com"
            text= EmailMessage()
            text['Subject']='ANNUAL DAY'
            text['From']= b
            text['To']= gmail1
            text.set_content('THE QRCORE IS AVAILABLE IN THE ATTACHMENT BELOW')
            with open(save_path, 'rb') as f:
                file_data= f.read()
                file_type = imghdr.what(f.name)
                file_name= f.name
            text.add_alternative(file_data, maintype='image', subtype=file_type, filename=file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(b,"hpnw loes eloe vczg")
                smtp.send_message(text)
                root.destroy()
                done=tk.Tk()
                done.title("Gmail send successfully")
                done.geometry("500x200")
                finish=tk.Label(done,text="WE HAVE SEND THE QR CODE TO YOUR GMAIL ID")
                finish.pack()
                done.mainloop()
        root = Tk()
        root.title("Student Information QR Code Generator")
        root.geometry("400x500")


        Label(root, text="Student's Name:").pack(pady=5)
        student_name_entry = Entry(root, width=40)
        student_name_entry.pack(pady=5)

        Label(root, text="Father's Name:").pack(pady=5)
        father_name_entry = Entry(root, width=40)
        father_name_entry.pack(pady=5)

        Label(root, text="Mother's Name:").pack(pady=5)
        mother_name_entry = Entry(root, width=40)
        mother_name_entry.pack(pady=5)
        gmail=tk.Label(root,text="Enter you gmail here:")
        Ent=tk.Entry(root,width=40)
        gmail.pack(pady=5)
        Ent.pack(pady=5)


        Label(root, text="Select Class:").pack(pady=5)
        class_var = StringVar(root)
        class_var.set("Select Class")
        class_dropdown = OptionMenu(root, class_var, "9", "10", "11", "12")
        class_dropdown.pack(pady=5)


        Label(root, text="Select Section:").pack(pady=5)
        section_var = StringVar(root)
        section_var.set("Select Section")
        section_dropdown = OptionMenu(root, section_var, "A", "B", "C", "D","commerce","humanities")
        section_dropdown.pack(pady=5)
        


        Button(root, text="Generate QR Code", command=generate_qr_code).pack(pady=10)


        qr_label = Label(root)
        qr_label.pack(pady=10)


        root.mainloop()
 
    elif not username1 or not password1:
        messagebox.showerror('Value missing', 'Input all values')
    else:
        messagebox.showerror('Invalid Input', 'Invalid Username or password')
login= tk.Tk()
login.title("Login")
login.geometry("500x200")
login.configure(bg='#000000')
bg = PhotoImage(file="E:\\school project\\new\\qr.png") 
label1 = tk.Label( login, image =bg) 
label1.place(x = 0, y = 0) 
name=tk.Label(text="Enter your username",bg='#000000',fg='#FFFD55',font=(25))
name.pack()
username=tk.Entry()
username.pack()


passwordkey=tk.Label(text="Enter your password",bg='#000000',fg='#FFFD55',font=(25) )
passwordkey.pack()
password=tk.Entry(show="*")
password.pack()

submit= tk.Button(text="submit",command=check)
submit.pack()

login.mainloop()
