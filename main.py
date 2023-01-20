from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_input.config(text = f"{km}")

window = Tk()
window.title("Mile to KM converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)


miles_label = Label(text="Miles")
miles_label.grid(row=0 , column=2)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1,column=0)


km_input = Label(text="0")
km_input.grid(row=1,column=1)


km_label = Label(text="Km")
km_label.grid(row=1,column=2)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)


window.mainloop()