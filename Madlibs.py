import tkinter as tk
from tkinter import messagebox
import time

# --- Main Application ---
root = tk.Tk()
root.title("Interactive Mad Libs")
root.geometry("600x400")
root.config(bg="#f2f2f2")

# --- Title Animation ---
title_label = tk.Label(root, text="🎭 Welcome to Mad Libs 🎭", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="blue")
title_label.place(rely=0.5, rely=0.1, anchor="center")

def animate_title():
    current_color = title_label.cget("fg")
    new_color = "red" if current_color == "blue" else "blue"
    title_label.config(fg=new_color)
    root.after(500, animate_title)  # repeat every 500ms

animate_title()

# --- Input Fields ---
char_label = tk.Label(root, text="Enter a Character:", font=("Arial", 12), bg="#f2f2f2")
char_label.place(relx=0.1, rely=0.3)

char_entry = tk.Entry(root, font=("Arial", 12))
char_entry.place(relx=0.5, rely=0.3, relwidth=0.35)

place_label = tk.Label(root, text="Enter a Place:", font=("Arial", 12), bg="#f2f2f2")
place_label.place(relx=0.1, rely=0.4)

place_entry = tk.Entry(root, font=("Arial", 12))
place_entry.place(relx=0.5, rely=0.4, relwidth=0.35)

object_label = tk.Label(root, text="Enter an Object:", font=("Arial", 12), bg="#f2f2f2")
object_label.place(relx=0.1, rely=0.5)

object_entry = tk.Entry(root, font=("Arial", 12))
object_entry.place(relx=0.5, rely=0.5, relwidth=0.35)

# --- Story Display ---
story_box = tk.Text(root, height=6, font=("Arial", 12), wrap="word", bg="white", fg="black")
story_box.place(relx=0.1, relx=0.65, relwidth=0.8)

# --- Functions ---
def generate_story():
    character = char_entry.get()
    place = place_entry.get()
    obj = object_entry.get()

    if not character or not place or not obj:
        messagebox.showwarning("Input Missing", "Please fill in all fields!")
        return

    story = f"""
    Once upon a time, {character} traveled to {place}.
    On the way, they found a magical {obj} that changed everything!
    """
    story_box.delete("1.0", tk.END)
    story_box.insert(tk.END, story)

def clear_story():
    char_entry.delete(0, tk.END)
    place_entry.delete(0, tk.END)
    object_entry.delete(0, tk.END)
    story_box.delete("1.0", tk.END)

# --- Buttons ---
generate_btn = tk.Button(root, text="✨ Generate Story", font=("Arial", 12, "bold"), bg="green", fg="white", command=generate_story)
generate_btn.place(relx=0.25, rely=0.9, relwidth=0.2, relheight=0.07)

clear_btn = tk.Button(root, text="🧹 Clear", font=("Arial", 12, "bold"), bg="red", fg="white", command=clear_story)
clear_btn.place(relx=0.55, rely=0.9, relwidth=0.2, relheight=0.07)

# --- Run ---
root.mainloop()