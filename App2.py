from tkinter import *
import csv
# Window setup
root = Tk()
root.title('CCSU Mobile App')
root.geometry("750x550")
root.resizable(0, 0)
root.configure(bg='lightblue')
# Logo
logo = PhotoImage(file="logo1.png")
logoLabel = Label(root, image=logo, bg='lightblue')
logoLabel.place(x=10, y=10)
# Load CSV data
calendar_data = []
buildings_data = []
faculty_data = []
with open("examfile.csv", newline='') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
if row.get('CalendarDate'):
calendar_data.append(row['CalendarDate'])
if row.get('Buildings'):
buildings_data.append(row['Buildings'])
if row.get('FacultyName'):
faculty_data.append(row['FacultyName'])
# Output label
output_label = Label(root, text="", justify="left",
bg='lightsteelblue', anchor="n", font=("Arial", 10))
output_label.place(x=200, y=220)
# Functions
def show_calendar():
output_label.config(text="\n".join(calendar_data))
def show_buildings():
output_label.config(text="\n".join(buildings_data))
def show_faculty():
output_label.config(text="\n".join(faculty_data))
def show_business():
text = "School of Business Departments\n\n" + "\n".join([
"• Accounting",
"• Finance",
"• Management & Organization",
"• Marketing",
"• Management Information Systems (MIS)",
"• Business Analytics"
])
output_label.config(text=text)
def show_mis():
text = "MIS Department Core Courses\n\n" + "\n".join([
"• Intro to MIS",
"• Database Management",
"• Systems Analysis & Design",
"• Business Analytics / Data Visualization",
"• Network & Information Security",
"• Project Management"
])
output_label.config(text=text)
# Button style
btn_style = {
"bg": "darkblue",
"fg": "white",
"width": 15
}

# Buttons row 1
Button(root, text='Calendar', command=show_calendar, **btn_style).place(x=150, y=90)
Button(root, text='Buildings', command=show_buildings, **btn_style).place(x=300, y=90)
Button(root, text='Faculty', command=show_faculty, **btn_style).place(x=450, y=90)
# Buttons row 2
Button(root, text='School of Business', command=show_business,
bg="#003399", fg="white", width=20).place(x=220, y=130)
Button(root, text='MIS Department', command=show_mis,
bg="#003399", fg="white", width=20).place(x=420, y=130)
# run main program
root.mainloop()
