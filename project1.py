import tkinter as tk
from calendar import day_abbr
#create main window
window = tk.Tk()
window.title("Student Performance Helper")
window.geometry("400x400")
#Stringvar for output
result_text = tk.StringVar()
#function
def calculate_grade():
scores = [
float(score1_entry.get()),
float(score2_entry.get()),
float(score3_entry.get())
]
average = sum(scores)/len(scores)
#if/else function for grade
if average >= 90:
grade = "A"
elif average >= 80:
grade = "B"
elif average >= 70:
grade = "C"
elif average >= 60:
grade = "D"
else:
grade = "F"
#display result
result_text.set("Average: " + str(round(average,2)) + " grade: "+ grade)
#function --> study hours
def calculate_hours():
hours = [
float(day1_entry.get()),
float(day2_entry.get()),
float(day3_entry.get())
]
total = sum(hours)
result_text.set("Total Study Hours: "+ str(total))
#clear
def clear_output():
result_text.set("")
#GUI ELEMENTS
#Score section
tk.Label(window,text="Enter Test Scores").pack()
score1_entry = tk.Entry(window)
score1_entry.pack()
score2_entry = tk.Entry(window)
score2_entry.pack()
score3_entry = tk.Entry(window)
score3_entry.pack()
tk.Button(window, text = "calculate grade", command=calculate_grade).pack(pady=5)
#study hours section
tk.Label(window,text="Enter study hours(3 days)").pack()
day1_entry = tk.Entry(window)
day1_entry.pack()
day2_entry = tk.Entry(window)
day2_entry.pack()
day3_entry = tk.Entry(window)
day3_entry.pack()
tk.Button(window,text = "Calculate Study Hours", command = calculate_hours).pack(pady=5)
#clear button
tk.Button(window, text = "clear output", command = clear_output).pack(pady=5)
#output label
tk.Label(window, textvariable=result_text,fg="blue").pack(pady = 20)
#run main program
window.mainloop()
