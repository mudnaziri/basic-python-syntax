#d = input("distance in KM: ")
#t = input("time in hour: ")                   # v = d / t
#velocity = int(d) / int(t) 
#print(velocity)

#i = input("current in ampire: ")
#r = input("risistance in ohm: ")                # v = i * r
#potential_difference =int(i) * int(r)
#print(potential_difference)

#file = open("mud.txt", "r")
#content = file.read()
#print(content)
#file.close()

import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x400")
root.configure(bg="light blue")

messag_label = tk.Label(root, text="Click a button below", font=("Arial", 12), bg = "light blue", fg = "blue")
messag_label.pack(pady=20)

def button_1():
    messag_label.config(text="hello sir!")

def button_2():
    messag_label.config(text="hello madam!")

def button_3():
    messag_label.config(text="hello everyone!")

def button_4():
    messag_label.config(text="what is on your mind!! ")
button = tk.Button(root, text="for male", command=button_1)
button.pack()
button_h = tk.Button(root, text ="for female", command = button_2)
button_h.pack()
button_m = tk.Button(root, text="for group", command=button_3)
button_m.pack()
button_n = tk.Button(root, text = "for surpirse", command = button_4)
button_n.pack()

root.mainloop()






