from tkinter import *
from datetime import date
root = Tk()
root.geometry("400x400")
root.title("Age Calculator")
def cal():
    try:
        year = date.today().year
        year_val = int(year_entry.get())

        if year_val>year:
            lbl1["text"] = "Your year is not valid"
        else:
            lbl1["text"] = f"You are {year - year_val} years old."
    except:
        lbl1["text"] = "Your input YEAR is not valid"

lbl_heading = Label(root, text="Age Calculator App", font=("Helvetica", 16, "bold"), fg="green")
lbl_heading.pack()

year_lbl = Label(root, text="Year: ")
year_lbl.pack()
year_entry = Entry(root)
year_entry.pack()

cal_btn = Button(root, text="Calculate", command=cal)
cal_btn.pack()

lbl1 = Label(root, text="")
lbl1.pack()
root.mainloop()
