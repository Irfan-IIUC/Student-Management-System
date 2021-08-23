from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk, Image

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1280x950+0+0")



        # ================== Variable =====================

        self.roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.address = StringVar()

        self.search_var = StringVar()
        self.search_txt = StringVar()





        l1 = Label(self.root, text="Student Management System", font=("Times New Roman",
             40, "bold"), fg="red", bg="darkGreen", bd=10, relief=GROOVE)
        l1.pack(side=TOP, fill=X)

        f1 = Frame(self.root, bd=10, relief=RIDGE, bg="darkGreen")
        f1.place(x=10, y=95, width=450, height=855)

        f2 = Frame(self.root, bd=10, relief=RIDGE, bg="darkGreen")
        f2.place(x=471, y=95, width=797, height=855)





        l2 = Label(f1, text="Manage Student", font=("Times New Roman",30, "bold"),
                   fg="white", bg="darkGreen")
        l2.pack(side=TOP, fill=X)

        l3 = Label(f1, text="Roll No", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l3.place(x=15, y=80)

        t1 = Entry(f1, textvariable=self.roll, font=("Times New Roman", 17))
        t1.place(x=150, y=80, width=260, height=30)

        l4 = Label(f1, text="Name", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l4.place(x=15, y=140)

        t2 = Entry(f1, textvariable=self.name, font=("Times New Roman", 17))
        t2.place(x=150, y=140, width=260, height=30)

        l5 = Label(f1, text="Email", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l5.place(x=15, y=200)

        t3 = Entry(f1, textvariable=self.email, font=("Times New Roman", 17))
        t3.place(x=150, y=200, width=260, height=30)

        l6 = Label(f1, text="Gender", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l6.place(x=15, y=260)

        cb = ttk.Combobox(f1, textvariable=self.gender, font=("Times New Roman", 17), state="readonly")
        cb["values"] = ("Male", "Female", "Others")
        cb.current(0)
        cb.place(x=150, y=260, width=260, height=30)

        l7 = Label(f1, text="Contact", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l7.place(x=15, y=320)

        t4 = Entry(f1, textvariable=self.contact, font=("Times New Roman", 17))
        t4.place(x=150, y=320, width=260, height=30)

        l8 = Label(f1, text="Date of Birth", font=("Times New Roman", 16, "bold"),
                   fg="red", bg="darkGreen")
        l8.place(x=15, y=380)

        t5 = Entry(f1, textvariable=self.dob, font=("Times New Roman", 17))
        t5.place(x=150, y=380, width=260, height=30)

        l9 = Label(f1, text="Address", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l9.place(x=15, y=440)

        self.t6 = Entry(f1, textvariable=self.address, font=("Times New Roman", 17))
        self.t6.place(x=150, y=440, width=260, height=30)





        # ============ Image =================

        i1 = Image.open("images/a.jpg")
        i1 = i1.resize((390, 220), Image.ANTIALIAS)
        i1 = ImageTk.PhotoImage(i1)
        l0 = Label(f1, image=i1)
        l0.image = i1
        l0.place(x=15, y=500)





        # ============== Button ==============

        f3 = Frame(f1, bd=10, relief=RIDGE, bg="darkGreen")
        f3.place(x=15, y=750, width=400, height=70)

        b1 = Button(f3, command=self.addStudent, text="Add", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b1.place(x=5, y=5, width=80, height=39)

        b2 = Button(f3, command=self.updateStudent, text="Update", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b2.place(x=100, y=5, width=80, height=39)

        b3 = Button(f3, command=self.deleteData, text="Delete", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b3.place(x=200, y=5, width=80, height=39)

        b4 = Button(f3, command=self.clearData, text="Clear", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b4.place(x=295, y=5, width=80, height=39)





        # ================ Right Frame =================

        l10 = Label(f2, text="Search By", font=("Times New Roman", 20, "bold"),
                   fg="red", bg="darkGreen")
        l10.place(x=15, y=15)

        cb1 = ttk.Combobox(f2, textvariable=self.search_var, font=("Times New Roman", 17), state="readonly")
        cb1["values"] = ("roll", "name", "email", "gender", "contact", "dob", "address")
        cb1.current(0)
        cb1.place(x=150, y=15, width=200, height=30)

        t7 = Entry(f2, textvariable=self.search_txt, font=("Times New Roman", 17))
        t7.place(x=365, y=15, width=200, height=30)

        b6 = Button(f2, command=self.searchBy, text="Search", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b6.place(x=580, y=15, width=80, height=32)

        b7 = Button(f2, command=self.showData, text="Show All", font=("Times New Roman", 15, "bold"), fg="white", bg="red")
        b7.place(x=675, y=15, width=90, height=32)





        # ================= Table ================

        f4 = Frame(f2, bd=10, relief=RIDGE, bg="darkGreen")
        f4.place(x=15, y=70, width=750, height=750)

        scroll_x = Scrollbar(f4, orient=HORIZONTAL)
        scroll_y = Scrollbar(f4, orient=VERTICAL)

        self.t = ttk.Treeview(f4, column=('roll', 'name', 'email', 'gender', 'contact',
        'dob', 'address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.t.xview)
        scroll_y.config(command=self.t.yview)

        self.t.heading("roll", text="Roll No")
        self.t.heading("name", text="Name")
        self.t.heading("email", text="Email")
        self.t.heading("gender", text="Gender")
        self.t.heading("contact", text="Contact No")
        self.t.heading("dob", text="Date of Birth")
        self.t.heading("address", text="Address")

        self.t["show"] = "headings"

        self.t.column("roll", width=100)
        self.t.column("name", width=100)
        self.t.column("email", width=100)
        self.t.column("gender", width=100)
        self.t.column("contact", width=100)
        self.t.column("dob", width=100)
        self.t.column("address", width=100)

        self.t.pack(fill=BOTH, expand=1)
        self.t.bind("<ButtonRelease-1>", self.selectData)
        self.showData()




    def addStudent(self):
        if self.roll.get() == "" or self.name.get() == "":
            messagebox.showerror("Message", "Roll number or Student Name\nis required !")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password=
                                           "root", database="projectsms1")

            my_cursor = conn.cursor()

            sql = 'insert into student values(%s, %s, %s, %s, %s, %s, %s)'
            data = (self.roll.get(), self.name.get(), self.email.get(), self.gender.get(), self.contact.get(), self.dob.get(), self.address.get())

            my_cursor.execute(sql, data)
            conn.commit()
            messagebox.showinfo("Message", "Data Inserted Successfully")
            self.showData()
            conn.close()





    def showData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=
        "root", database="projectsms1")

        my_cursor = conn.cursor()

        my_cursor.execute('select * from student')
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.t.delete(*self.t.get_children())

            for i in row:
                self.t.insert("", END, values=i)

            conn.commit()

        conn.close()





    def updateStudent(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=
                                       "root", database="projectsms1")

        my_cursor = conn.cursor()

        sql = 'update student set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll=%s'
        data = (self.name.get(), self.email.get(), self.gender.get(), self.contact.get(), self.dob.get(), self.address.get(), self.roll.get())

        my_cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Message", "Data Updated Successfully")
        self.showData()
        conn.close()





    def selectData(self, ev):
        x = self.t.focus()
        y = self.t.item(x)
        z = y["values"]

        print(z)

        self.roll.set(z[0])
        self.name.set(z[1])
        self.email.set(z[2])
        self.gender.set(z[3])
        self.contact.set(z[4])
        self.dob.set(z[5])
        self.address.set(z[6])





    def deleteData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=
                                       "root", database="projectsms1")
        my_cursor = conn.cursor()

        sql = 'delete from student where roll=%s'
        data = (self.roll.get(),)

        my_cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Message", "Data deleted successfully")
        self.showData()
        conn.close()





    def clearData(self):
        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.address.set("")





    def searchBy(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=
        "root", database="projectsms1")

        my_cursor = conn.cursor()

        my_cursor.execute('select * from student where '+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.t.delete(*self.t.get_children())

            for i in row:
                self.t.insert("", END, values=i)

            conn.commit()

        conn.close()




root = Tk()
ob = student(root)
root.mainloop()