from tkinter import *
window = Tk()
window.title("Mile to Km convertor")
window.minsize(width=200, height=100)
window.config(padx = 20, pady = 20)

def button_clicked():
    number_label["text"] = int(input.get())*1.609

miles_label = Label(text="Miles", font=("Ariel", 12, "normal"))
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to", font=("Ariel", 12, "normal"))
is_equal_to_label.grid(column=0, row=1)
km_label = Label(text="Km", font=("Ariel", 12, "normal"))
km_label.grid(column=2, row=1)
number_label= Label(text="0",  font=("Ariel", 12, "normal"))
number_label.grid(column=1, row=1)



button = Button(text = "Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
