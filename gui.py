import tkinter as tk

def create_window():
    window = tk.Tk()
    menu = tk.Menu(window)
    window.config(menu=menu)
    view_menu = tk.Menu(menu)
    menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Blue and Silver", command=blue_and_silver)
    view_menu.add_command(label="Red and Blue", command=red_and_blue)
    # Add placeholders for the various add-ons here
    return window

def blue_and_silver():
    window.config(bg='silver')
    # Change the inside color to blue
    # Change the text color depending on the darkness of the background

def red_and_blue():
    window.config(bg='blue')
    # Change the inside color to red
    # Change the text color depending on the darkness of the background

window = create_window()
window.mainloop()