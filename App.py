from tkinter import *
import csv
#Main window
root = Tk()
root.title('CCSU Mobile App')
root.geometry("770x550")
root.resizable(0, 0)
root.configure(bg='light blue')
#Load logo from the file
logo = PhotoImage(file="logo1.png") # or logo2.png
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=10, y=10)
# Load CSV data into lists
#create empty lists
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
bg="light blue", anchor="nw", font=("Arial", 10))
output_label.place(x=50, y=120, width=600, height=320)
# Button functions
def show_calendar():
output_label.config(text="\n".join(calendar_data))
def show_buildings():
output_label.config(text="\n".join(buildings_data))
def show_faculty():
output_label.config(text="\n".join(faculty_data))
# Buttons (horizontal)
button1 = Button(root, text='Calendar', command=show_calendar,
bg="light green", width=15)
button1.place(x=160, y=300)
button2 = Button(root, text='Buildings', command=show_buildings,
bg="light green", width=15)
button2.place(x=320, y=300)
button3 = Button(root, text='Faculty', command=show_faculty,
bg="light green", width=15)
button3.place(x=480, y=300)
#run the main loop
root.mainloop()
