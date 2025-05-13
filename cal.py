import tkinter as tk
from tkinter import ttk

def velocity():
    new_window=tk.Toplevel(root)
    new_window.title("Velocity Calculator")
    new_window.geometry("300x300")

    entry1=tk.Entry(new_window)
    entry1.pack(pady=5)
    entry2=tk.Entry(new_window)
    entry2.pack(pady=5)

    def calculate_velocity():
        try:
            d = float(entry1.get())
            t=  float(entry2.get())
            velocity=d/t
            la.config(text=f"velocity: {velocity:.2f} m/s")
        except ValueError:
            la.config(text="invalid value")
        except ZeroDivisionError:
            la.config("time can't be zero")

    def calculate_distance():
        try:
            v = float(entry1.get())
            t=  float(entry2.get())
            distance=v*t
            la.config(text=f"Distance: {distance:.2f} m")
        except ValueError:
            la.config(text="invalid value")

    def calculate_time():
        try:
            d = float(entry1.get())
            v=  float(entry2.get())
            time=d/v
            la.config(text=f"velocity: {time:.2f} s")
        except ValueError:
            la.config(text="invalid value")
        except ZeroDivisionError:
            la.config("velocity can't be zero")

        

    la=ttk.Label(new_window,text="Result appear here")
    la.pack(pady=5)

    bu=ttk.Button(new_window,text="velocity",command=calculate_velocity)
    bu.pack(pady=5)
    but=ttk.Button(new_window,text="Distance",command=calculate_distance)
    but.pack(pady=5)
    but=ttk.Button(new_window,text="time",command=calculate_time)
    but.pack(pady=5)
    close_bu=ttk.Button(new_window,text="close",command=new_window.destroy)
    close_bu.pack(pady=5)

def current():
    new_window=tk.Toplevel(root)
    new_window.title("Current Calculator")
    new_window.geometry("300x300")

    entry1=tk.Entry(new_window)
    entry1.pack(pady=5)
    entry2=tk.Entry(new_window)
    entry2.pack(pady=5)

    def calculate_current():
        try:
            q = float(entry1.get())
            t=  float(entry2.get())
            current=q/t
            la.config(text=f"Current: {current:.2f} Am")
        except ValueError:
            la.config(text="invalid value")
        except ZeroDivisionError:
            la.config("time can't be zero")

    def calculate_charge():
        try:
            i = float(entry1.get())
            t=  float(entry2.get())
            charge=i*t
            la.config(text=f"Charge: {charge:.2f} Co")
        except ValueError:
            la.config(text="invalid value")

    def calculate_time():
        try:
            q = float(entry1.get())
            i=  float(entry2.get())
            time=q/i
            la.config(text=f"Time: {time:.2f} s")
        except ValueError:
            la.config(text="invalid value")
        except ZeroDivisionError:
            la.config("Current can't be zero")

        

    la=ttk.Label(new_window,text="Result appear here")
    la.pack(pady=5)

    bu=ttk.Button(new_window,text="velocity",command=calculate_current)
    bu.pack(pady=5)
    but=ttk.Button(new_window,text="Distance",command=calculate_charge)
    but.pack(pady=5)
    but=ttk.Button(new_window,text="time",command=calculate_time)
    but.pack(pady=5)
    close_bu=ttk.Button(new_window,text="close",command=new_window.destroy)
    close_bu.pack(pady=5)

root=tk.Tk()
root.title("Physics Calculator")
root.geometry("300x300")

button=tk.Button(root,text="velocity",command=velocity)
button.pack(pady=5)
button=tk.Button(root,text="current",command=current)
button.pack(pady=5)

root.mainloop()