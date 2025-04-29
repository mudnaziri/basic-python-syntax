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
root.title("Addition ")
root.geometry("400x400")
root.config(bg = "orange")

mud_label = tk.Label(root, text ="Addition", font = ("Arial", 20), bg ="orange", fg = "green")
mud_label.pack()

entry1 =tk.Entry(root, font =("Arial", 40))
entry1.pack()

entry2 = tk.Entry(root, font=("Arial",40))
entry2.pack()

def addition():
    try:
       num1 = int(entry1.get())
       num2 = int(entry2.get())
       result = num1 + num2
       mud_label.config(text = "Result: " + str(result)) 
    except ValueError:
         mud_label.config(text = "Please enter valid numbers")

button = tk.Button(root, text ="add", command = addition, font=("Arial",50)).pack()

root.mainloop()  