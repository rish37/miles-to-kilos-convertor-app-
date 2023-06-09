#importing Tkinter and ttk

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
	mile_input = entry_int.get()
	km_output = mile_input*1.61
	output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly')
window.title('Calculator')
window.geometry('300x150')

#title

title_labl = ttk.Label(master = window, text = 'miles to Kilo', font = 'Arial 24 bold')
title_labl.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_lable = ttk.Label(master = window, text = 'output', font = 'Arial 24', textvariable = output_string)
output_lable.pack()

window.mainloop()