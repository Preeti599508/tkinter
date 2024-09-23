import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# print("first name": firstname, "last name": lastname)
# print("Title": title, "Age": age, "Nationality": nationality)
# print("Courses": numcourses, "Semester": numsemester)
# print("Registration status": registration_status)
# print(".............................................")
# conn=sqlite3.connect('data.do')
# conn.close()
root=tk.Tk()
root.title("Data Entry Form ")

frame=tk.Frame(root)
frame.pack()

user_info_frame=tk.LabelFrame(frame,text="User  Information")
user_info_frame.grid(row= 0,column=0,padx=20,pady=20)

first_name_label=tk.Label(user_info_frame,text="firstname")
first_name_label.grid(row=0,column=0)
last_name_label=tk.Label(user_info_frame,text="lastname")
last_name_label.grid(row=0,column=1)

first_name_entry=tk.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry=tk.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

title_label=tk.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame,values=['','Mr','Mrs','other'])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tk.Label(user_info_frame,text="age")
age_spinbox=tk.Spinbox(user_info_frame, from_ = 18  , to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tk.Label(user_info_frame,text="Nationality")
nationality_combobox=ttk.Combobox(user_info_frame,values=["Asia","America","India","South africa","Europe"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)



root.mainloop()