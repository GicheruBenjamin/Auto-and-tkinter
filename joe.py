import tkinter as tk
import pyautogui

def update_position():
    x, y = pyautogui.position()
    x_offset, y_offset = 20, 20  # Distance to allow hovering
    root.geometry(f"250x100+{x + x_offset}+{y + y_offset}")

    # Update label text with cursor position in pixels
    position_label.config(text=f"X: {x}px\nY: {y}px")

    root.after(10, update_position)  # Update every 10 milliseconds

def on_click(event):
    x, y = pyautogui.position()
    print(f"Mouse clicked at X: {x}px, Y: {y}px")

root = tk.Tk()
root.title("Mouse Position Tracker")

# Set the app at the center-top of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = screen_width // 2 - 125  # Centered horizontally
y_position = 0  # At the top of the screen
root.geometry(f"250x100+{x_position}+{y_position}")

# Style the app
root.configure(bg='#f0f0f0')  # Light gray background color

# Label to display cursor position
position_label = tk.Label(root, text="X: 0px\nY: 0px", font=('Arial', 14), bg='#f0f0f0')
position_label.pack(pady=20)

# Call the update_position function to continuously update the window position
update_position()

root.config(cursor="arrow")

# Binding the left click event 
root.bind("<Button-1>", on_click)

root.mainloop()
